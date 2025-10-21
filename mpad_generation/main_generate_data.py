# Core
import os
import sys
import io
import json
from time import time
import random
import shutil
import base64
# import asyncio
# import traceback
from math import ceil, floor
from collections import Counter
from typing import Any, List, Dict, Optional
from pathlib import Path

# Image processing
import numpy as np
import cv2 as cv
from PIL import Image, ImageDraw, ImageOps, ImageFilter
import xml.etree.ElementTree as ET

# Torch
import torch
import torch.nn.functional as F
import torch.multiprocessing as mp
from torch.utils.data import DataLoader, Dataset
import torch.distributed as dist
from torch.utils.data.distributed import DistributedSampler

# Torchvision
import torchvision
from torchvision.transforms import functional as TF

# HuggingFace & Diffusers
from diffusers import StableDiffusionGLIGENPipeline
from diffusers.utils import load_image
from transformers import CLIPProcessor, CLIPModel

# CLI & Progress
import argparse
from tqdm import tqdm

# Project-specific
import loader
from utils.metadata import (
    PASCAL_VOC_NOVEL_CATEGORIES,
    PASCAL_VOC_BASE_CATEGORIES,
    coco2voc,
    voc2coco,
    COCO_NOVEL_CATEGORIES,
    COCO_BASE_CATEGORIES,
    COCO_CATEGORIES,
    voc_fine_grained_classes,
    coco_fine_grained_classes,
    stable_inpaint_path,
    stable_diffusion_path,
    feature_dir,
    dataset_path,
    text_encoder_path,
    unet_path,
)
from utils.prompting import prompting, prompting3_coco, prompting4
from utils.functions import *

# Initiate new index for new data images and annotations
New_Index = 9962
mix_up_alpha = 0.9
BOX_TRESHOLD = 0.25
TEXT_TRESHOLD = 0.85
NUM_INFERENCE_STEP = 80

powerpaint_args = {
    'stable_inpaint_name': stable_inpaint_path,
    'stable_diffusion_name': stable_diffusion_path,
    'unet_name': unet_path,
    "text_encoder_name": text_encoder_path,
    'device': torch.device('cuda' if torch.cuda.is_available() else 'cpu'),
}

Log_Edited_Image = {}


class CustomImageDataset(Dataset):
    def __init__(self, dict_data):
        self.dict_data = dict_data

    def __len__(self):
        return len(self.dict_data)

    def __getitem__(self, idx):
        return idx


def run_inference_background(rank, world_size, dicts):
    is_coco = dicts['coco']

    global powerpaint_args, New_Index
    Output_Images = dicts['Output_Images']
    Output_Annotations = dicts['Output_Annotations']
    Log_Image_Path = dicts['Log_Image_Path']

    ddp_setup(rank, world_size)
    painter = loader.getPowerPaint(**powerpaint_args)
    painter = painter.to(rank)

    bg_sim = dicts['background_similarity']['use']
    bg_clut = dicts['background_clutter']['use']
    bg_ran = dicts['background_random']['use']
    fg_sim = dicts['foreground_similarity']['use']
    fg_fg = dicts['foreground_fine_grained']['use']
    txt_ppt = dicts['text_prompt']['use']

    augment_multi_scale = dicts['multi-scale-object']['use']
    novel_classes = dicts['novel_classes']
    batch_size = dicts['batch_size']
    topk = dicts['num-fine-grained']
    mix_up_alpha = dicts['mix-up-alpha']
    momemtum = dicts['momemtum']

    id2name, name2id = {}, {}
    if is_coco:
        id2name = {idx : class_name for idx, class_name in enumerate(COCO_CATEGORIES)}
        name2id = {class_name : idx for idx, class_name in enumerate(COCO_CATEGORIES)}
    else:
        name2id = {name: idx for idx, name in enumerate(novel_classes)}

    list_novel_classes = []
    global_dataset = []
    for i in range(5):
        shot_idx = i+1
        for sub_data, novel_cls in zip(dicts[f'dataset_shot_idx_{shot_idx}'], novel_classes):
            global_dataset.extend(sub_data)
            list_novel_classes.extend([novel_cls] * len(sub_data))

        dataloader = DataLoader(CustomImageDataset(global_dataset),
                                batch_size=batch_size, shuffle=False,
                                sampler=DistributedSampler(global_dataset))

        # DUMP
        # dump_file = {
        #     "global_dataset" : global_dataset,
        #     "list_novel_classes" : list_novel_classes,
        # }
        # out = Path("data.json")
        # with out.open("w", encoding="utf-8") as f:
        #     json.dump(dump_file, f, ensure_ascii=False, indent=2)
        # exit()

        saved_annotations, saved_images = [], []

        for indx in tqdm(dataloader):
            dict_input_data = [global_dataset[i] for i in indx]
            sub_list_novel_classes = [list_novel_classes[i] for i in indx]

            image_path_list = [i['file_name'] for i in dict_input_data]
            annotations = [i['annotations'] for i in dict_input_data]

            dict_data = preprocess2(image_path_list, annotations, augment_multi_scale,
                                    dicts['multi-scale-object']['p'])

            masks = dict_data["masks"]
            images = dict_data["images"]
            labels = dict_data["labels"]
            shape = dict_data["shape"].cpu().numpy()
            pad_shape = dict_data["pad_shape"]
            pil_images = dict_data["pil_images"]
            unresized_masks = dict_data["unresized_masks"]
            choiced_index_list = dict_data["choiced_index_list"]
            expanded_bbox = dict_data["expanded_bbox"]

            class_A, class_B, Prompt_A, Prompt_B = [], [], [], []

            prompt_func = prompting3_coco if is_coco else prompting4
            list_fine_grained_class = coco_fine_grained_classes if is_coco else voc_fine_grained_classes

            for base_cls, novel_cls in zip([i['classname'] for i in labels], sub_list_novel_classes):
                novel_prompt, attr = prompt_func(novel_cls, dicts['foreground_fine_grained']['p'],
                                                 num_fine_grained_cls=topk)
                base_prompt = novel_prompt
                temp_base_class = novel_cls

                if fg_fg and random.uniform(0, 1) < dicts['foreground_fine_grained']['p']:
                    fg_clss = random.choice(list_fine_grained_class[novel_cls][:topk]).lower()
                    novel_prompt = prompting(fg_clss)
                    base_prompt = prompting(fg_clss)

                if fg_sim and random.uniform(0, 1) < dicts['foreground_similarity']['p']:
                    temp_base_class = base_cls
                    # if is_coco:
                    #     temp_base_class = id2name[base_cls]

                    novel_prompt, _ = prompt_func(novel_cls,
                                                  dicts['foreground_fine_grained']['p'],
                                                  num_fine_grained_cls=topk, apply_mixup=True)

                if txt_ppt and random.uniform(0, 1) < dicts['text_prompt']['p']:
                    prompt_list = dicts['text_prompt']['prompt'][novel_cls]
                    novel_prompt = random.choice(prompt_list)
                    base_prompt = random.choice(prompt_list)

                class_A.append(novel_cls)
                class_B.append(temp_base_class)
                Prompt_A.append(novel_prompt)
                Prompt_B.append(base_prompt)

            try:
                edited_images, _ = torch_edit(painter, images, masks, Prompt_A, Prompt_B,
                                               mix_up_alpha=mix_up_alpha, num_inference_steps=NUM_INFERENCE_STEP,
                                               momemtum=momemtum)
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
                continue

            if not edited_images[0]:
                continue

            for i in range(len(dict_input_data)):
                New_Index += 1
                result_pil = edited_images[i]
                mask = unresized_masks[i]
                original_shape = shape[i]
                pA = Prompt_A[i]
                pB = Prompt_B[i]
                original_image_pil = pil_images[i]
                size = original_image_pil.size
                output_image = result_pil.resize(size)
                f_name = dict_input_data[i]['file_name'].split('/')[-1].split('.')[0]
                shot_idx = dict_input_data[i]["shot_idx"]
                class_idx = dict_input_data[i]["class_idx"]
                novel_cls = sub_list_novel_classes[i]
                novel_class_id = name2id[novel_cls]
                image_name = f"syn_{shot_idx}_{novel_class_id}_{f_name}.jpg"
                #datasets / coco / JPEGImages / 000089.jpg --> 000089
                #image_name = f"syn{f_name}_{New_Index:08d}.jpg"
                #image_name = f"syn_{shot_idx}_{class_idx}_{f_name}.jpg"
                process_obj = [class_B[i], class_A[i], expanded_bbox[i]]
                iter_process = choiced_index_list[i]
                output_image.save(os.path.join(Output_Images, image_name))

                if is_coco:
                    init_xml_path = dict_input_data[i]['anno_file']

                    tree = ET.parse(init_xml_path)
                    root = tree.getroot()
                    for child in root:
                        if child.tag == 'filename':
                            child.text = image_name
                    for iter_annotation, obj in enumerate(root.findall("object")):
                        o_bbox = process_obj[2]
                        if iter_process == iter_annotation:
                            obj.find("name").text = process_obj[1]
                            bndbox = obj.find("bndbox")
                            bndbox.find('xmin').text = str(o_bbox[0])
                            bndbox.find('ymin').text = str(o_bbox[1])
                            bndbox.find('xmax').text = str(o_bbox[2])
                            bndbox.find('ymax').text = str(o_bbox[3])
                            ET.SubElement(obj, 'Text_prompt', pA=pA, pB=pB, pname=obj.find("name").text)
                            ET.SubElement(obj, 'all_name', all_class=process_obj[0] + "_" + process_obj[1])

                    ET.ElementTree(root).write(os.path.join(Output_Annotations, image_name.replace(".jpg", ".xml")),
                                               encoding='utf-8', xml_declaration=False)
                    Log_Edited_Image[New_Index] = pA + "_" + pB + image_path_list[i]

                else:
                    init_xml_path = dict_input_data[i]['anno_file']

                    tree = ET.parse(init_xml_path)
                    root = tree.getroot()
                    for child in root:
                        if child.tag == 'filename':
                            child.text = image_name
                    for iter_annotation, obj in enumerate(root.findall("object")):
                        o_bbox = process_obj[2]
                        if iter_process == iter_annotation:
                            obj.find("name").text = process_obj[1]
                            bndbox = obj.find("bndbox")
                            bndbox.find('xmin').text = str(o_bbox[0])
                            bndbox.find('ymin').text = str(o_bbox[1])
                            bndbox.find('xmax').text = str(o_bbox[2])
                            bndbox.find('ymax').text = str(o_bbox[3])
                            ET.SubElement(obj, 'Text_prompt', pA=pA, pB=pB, pname=obj.find("name").text)
                            ET.SubElement(obj, 'all_name', all_class=process_obj[0] + "_" + process_obj[1])

                    ET.ElementTree(root).write(os.path.join(Output_Annotations, image_name.replace(".jpg", ".xml")),
                                               encoding='utf-8', xml_declaration=False)
                    Log_Edited_Image[New_Index] = pA + "_" + pB + image_path_list[i]


    # if is_coco:
    #     # save data for coco dataset
    #
    #     synthesis_dataset = {
    #         'images': saved_images,
    #         'annotations': saved_annotations,
    #     }
    #     # check stats:
    #     stas = []
    #     id2class = {i['id']: i['name'] for i in COCO_NOVEL_CATEGORIES}
    #     for obj in saved_annotations:
    #         class_id = int(obj['category_id'].split(' ')[-1]) if isinstance(obj['category_id'], str) else obj[
    #             'category_id']
    #         if class_id in id2name.keys():
    #             stas.append(id2name[class_id])
    #
    #     print('Global classes', Counter(stas))
    #     print('Sum counter(stas)', sum(Counter(stas).values()))
    #
    #     # saved_annotations
    #     # for i in saved_images:
    #     #     for val in i.values():
    #     #         if type(val).__module__ == np.__name__:
    #     #             val = val.tolist()
    #
    #     # for i in saved_annotations:
    #     #     for val in i.values():
    #     #         if type(val).__module__ == np.__name__:
    #     #             val = val.tolist()
    #     torch.save(synthesis_dataset, os.path.join(Output_Annotations, f'data_{rank}.pt'))


def default_argument_parser():
    """
    Create a parser with some common arguments used by DeFRCN users.

    Returns:
        argparse.ArgumentParser:
    """
    parser = argparse.ArgumentParser(description="Khoa custom")
    parser.add_argument("--gendata-folder", help="path to synthesis data folder")
    parser.add_argument("--num-ins", type=int, default=100, help="The number of generated instance per novel class")
    parser.add_argument("--bz", type=int, default=2, help="the batch-size")

    parser.add_argument("--bg-sim", action="store_true")
    parser.add_argument("--bg-clutter", action="store_true")
    parser.add_argument("--bg-rand", action="store_true")

    parser.add_argument("--fg-sim", action="store_true")
    parser.add_argument("--mix-up", type=float, default=0.9)
    parser.add_argument("--momemtum", type=float, default=0.99)
    parser.add_argument("--fg-fg", action="store_true")
    parser.add_argument("--fg-rand", action="store_true")
    parser.add_argument("--txt-ppt", action="store_true")
    parser.add_argument("--p-multi-scale", type=float, default=0)
    parser.add_argument("--p-fg-sim", type=float, default=0)
    parser.add_argument("--sid", type=str, default="t1")
    parser.add_argument("--coco", action="store_true")
    parser.add_argument("--num-fine-grained", type=int, default=4,
                        help="The number of fine-grained classes per novel class")

    return parser


def get_features(features, in_features=['res2', 'res3']):
    return torch.cat([features[f] for f in in_features], dim=1)


def main(dicts):
    world_size = torch.cuda.device_count()
    print(f"world_size : {world_size}")

    with torch.no_grad():
        mp.spawn(run_inference_background, args=(world_size, dicts,), nprocs=world_size, join=True)

    # Save image log to be eddited
    with open(Log_Image_Path, 'w+') as file:
        for key, value in Log_Edited_Image.items():
            file.write(f"{key}: {value}\n")


if __name__ == "__main__":

    args = default_argument_parser().parse_args()
    print('args: ', args)

    RANDOM_SEED = 42
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)
    torch.manual_seed(RANDOM_SEED)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(RANDOM_SEED)
        torch.cuda.manual_seed_all(RANDOM_SEED)
    print(f"Random seed set to: {RANDOM_SEED}")

    FolderForGenVersion = args.gendata_folder # datasets/coco/
    max_num_novel_ins = args.num_ins

    #general_p_bg = 1 / max(args.bg_sim + args.bg_clutter + args.bg_rand, 1)
    general_p_bg = 1
    general_p_fg = 1 / max(args.fg_fg + args.fg_rand, 1)


    dicts = {}
    dicts['background_similarity'] = {"use": args.bg_sim, 'p': general_p_bg}
    dicts['background_clutter'] = {"use": args.bg_clutter, 'p': general_p_bg}
    dicts['background_random'] = {"use": args.bg_rand, 'p': general_p_bg}
    dicts['foreground_similarity'] = {"use": args.fg_sim, 'p': args.p_fg_sim}
    dicts['foreground_fine_grained'] = {"use": args.fg_fg, 'p': 0.8}
    dicts['text_prompt'] = {"use": args.txt_ppt, 'p': 1.0}
    dicts['multi-scale-object'] = {"use": True, 'p': args.p_multi_scale}
    dicts['num-fine-grained'] = args.num_fine_grained
    dicts['batch_size'] = args.bz
    dicts['mix-up-alpha'] = args.mix_up
    dicts['momemtum'] = args.momemtum
    dicts['coco'] = args.coco

    print(dicts)
    num_remove = 0
    is_coco = args.coco

    dataset = []
    choose_ids = []
    base_feature = []
    base_entropy = []
    removed_id_list = []
    in_features = ['res2', 'res3', 'res4', 'res5']

    VOC_DATASET = [(0, 'voc_2007_trainval', "VOC2007", "trainval"),
                   (1, 'voc_2012_trainval', "VOC2012", "trainval"),]
    sid = args.sid
    COCO_DATASET = [(sid, 'FS-OWODB', "coco", "t1")] # (id_dataset, name, dirname, split)

    if is_coco:
        novel_classes = COCO_NOVEL_CATEGORIES[sid]
        base_classes = COCO_BASE_CATEGORIES[sid]
        for id_dataset, name, dirname, split in COCO_DATASET:
            tic = time()
            data, removed_id, choose_id = load_filtered_voc_instances(name, os.path.join(dataset_path, dirname), split,
                                                                      base_classes,
                                                                      max_instance=None)  # choose base Images

            dataset.extend(data)
            # datasets : [{'file_name': 'datasets/coco/JPEGImages/000089.jpg', 'anno_file': 'datasets/coco/Annotations/000089.xml', 'image_id': '000089', 'shot_idx': 3, 'class_idx': 8, 'height': 374, 'width': 500, 'annotations': [{'category_id': 14, 'classname': 'person', 'bbox': [19, 6, 183, 355], 'bbox_mode': 'XYXY_ABS'}, {'category_id': 14, 'classname': 'person', 'bbox': [97, 214, 429, 374], 'bbox_mode': 'XYXY_ABS'}, {'category_id': 14, 'classname': 'person', 'bbox': [331, 139, 455, 366], 'bbox_mode': 'XYXY_ABS'}, {'category_id': 8, 'classname': 'chair', 'bbox': [21, 50, 317, 291], 'bbox_mode': 'XYXY_ABS'}]
            print('loaded {} with {} images, removed {}, take {:0.5f}s:'.format(name, len(data), len(removed_id), time() - tic)) # loaded FS_OWODB with 100 images, removed 0, take 0.00601s:
            #print(f"datasets : {dataset}, data : {data}")
            with open(os.path.join("datasets", dirname, "ImageSets", f"Main/{sid}" + ".txt")) as f:  # datasets/coco/ImageSets/Main/t1.txt
                novel_classes_fileids = np.loadtxt(f, dtype=str)

            # 예: {'person': [], 'car': [], 'dog': [], ...}
            fileids_per_novel_classes = [[] for _ in novel_classes]
            annotation_dir = os.path.join("datasets", dirname, "Annotations")
            for fileid in novel_classes_fileids:
                xml_path = os.path.join(annotation_dir, f"{fileid}.xml")

                try:
                    # XML 파일 파싱
                    tree = ET.parse(xml_path)
                    root = tree.getroot()

                    # 모든 object 태그에서 클래스 이름 추출
                    for obj in root.findall("object"):
                        class_name = obj.find("name").text

                        # 해당 클래스가 novel_class 리스트에 있으면 추가
                        if class_name in novel_classes:
                            fileids_per_novel_classes[novel_classes.index(class_name)].append(fileid)
                except Exception as e:
                    print(f"Error parsing {xml_path}: {e}")
                    continue
            # for idx, l in enumerate(fileids_per_novel_classes):
            #     print(f"{novel_classes[idx]}: {len(l)} images")

    else:
        novel_classes = COCO_NOVEL_CATEGORIES[sid]
        base_classes = COCO_BASE_CATEGORIES[sid]
        # dicts['meta_VOC_info'] = {1: meta_VOC_info_1,
        #                 2: meta_VOC_info_2,
        #                 3: meta_VOC_info_3}[sid]

        for id_dataset, name, dirname, split in COCO_DATASET:
            tic = time()
            data, removed_id, choose_id = load_filtered_voc_instances(name, os.path.join(dataset_path, dirname), split,
                                                                      base_classes,
                                                                      max_instance=None)  # choose base Images

            ### get base feature and entropy
            Name_Base = "Base_all_{}_{}_tensor_vit.pt"
            # Name_Base = "Base_all_{}_{}_tensor_resnet.pt" # resnet101
            # Name_Base = "Base_all_{}_{}_tensor_resnet50.pt"
            entropy = torch.load(os.path.join(feature_dir, Name_Base.format('entropy', dirname.lower())))[choose_id]

            Name_Base = "Base_all_{}_{}_tensor.pt"
            print(os.path.join(feature_dir, Name_Base.format('feature', dirname.lower())))
            feature = torch.load(os.path.join(feature_dir, Name_Base.format('feature', dirname.lower())))

            feature = get_features(feature, in_features=in_features)[choose_id]
            base_feature.append(feature)
            base_entropy.append(entropy)

            dataset.extend(data)
            print('loaded {} with {} images, removed {}, take {:0.5f}s:'.format(name, len(data), len(removed_id), time() - tic)) # loaded FS_OWODB with 100 images, removed 0, take 0.00601s:
            print(f"datasets : {dataset}, data : {data}")
            with open(os.path.join("datasets", dirname, "ImageSets", f"Main/{sid}" + ".txt")) as f:  # datasets/coco/ImageSets/Main/t1.txt
                novel_classes_fileids = np.loadtxt(f, dtype=str)

            # 예: {'person': [], 'car': [], 'dog': [], ...}
            fileids_per_novel_classes = [[] for _ in novel_classes]
            annotation_dir = os.path.join("datasets", dirname, "Annotations")
            for fileid in novel_classes_fileids:
                xml_path = os.path.join(annotation_dir, f"{fileid}.xml")

                try:
                    # XML 파일 파싱
                    tree = ET.parse(xml_path)
                    root = tree.getroot()

                    # 모든 object 태그에서 클래스 이름 추출
                    for obj in root.findall("object"):
                        class_name = obj.find("name").text

                        # 해당 클래스가 novel_class 리스트에 있으면 추가
                        if class_name in novel_classes:
                            fileids_per_novel_classes[novel_classes.index(class_name)].append(fileid)
                except Exception as e:
                    print(f"Error parsing {xml_path}: {e}")
                    continue
            for idx, l in enumerate(fileids_per_novel_classes):
                print(f"{novel_classes[idx]}: {len(l)} images")

    num_novel_classes = len(novel_classes)
    print(f"sid = {sid}, num_novel_classes = {num_novel_classes}, novel_classes : {novel_classes}")
    # sid = t1, num_novel_classes = 20, novel_classes: ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car',
    #                                                   'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike',
    #                                                   'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
    dicts['dataset'] = [[] for _ in range(num_novel_classes)]
    base_datasets_per_shot_idx = [[] for _ in range(5)]
    for data in dataset:
        shot_idx = data["shot_idx"]
        base_datasets_per_shot_idx[shot_idx-1].append(data)

    for i in range(5):
        shot_idx = i+1
        dicts[f'dataset_shot_idx_{shot_idx}'] = [[] for _ in range(num_novel_classes)]
        if args.bg_rand:
            n_bg_rand = int(max_num_novel_ins * general_p_bg)
            for id_cls in range(num_novel_classes):
                dicts[f'dataset_shot_idx_{shot_idx}'][id_cls].extend(random.sample(base_datasets_per_shot_idx[i], n_bg_rand))

    # if args.bg_rand:
    #     n_bg_rand = int(max_num_novel_ins * general_p_bg)
    #     for id_cls in range(num_novel_classes):
    #         dicts['dataset'][id_cls].extend(dataset[id_cls * n_bg_rand:(id_cls + 1) * n_bg_rand])
    # datasets : [{'file_name': 'datasets/coco/JPEGImages/000089.jpg', 'anno_file': 'datasets/coco/Annotations/000089.xml', 'image_id': '000089', 'shot_idx': 3, 'class_idx': 8, 'height': 374, 'width': 500, 'annotations': [{'category_id': 14, 'classname': 'person', 'bbox': [19, 6, 183, 355], 'bbox_mode': 'XYXY_ABS'}, {'category_id': 14, 'classname': 'person', 'bbox': [97, 214, 429, 374], 'bbox_mode': 'XYXY_ABS'}, {'category_id': 14, 'classname': 'person', 'bbox': [331, 139, 455, 366], 'bbox_mode': 'XYXY_ABS'}, {'category_id': 8, 'classname': 'chair', 'bbox': [21, 50, 317, 291], 'bbox_mode': 'XYXY_ABS'}]

    # if args.bg_rand:
    #     n_bg_rand = int(max_num_novel_ins * general_p_bg)
    #     for id_cls in range(num_novel_classes):
    #         existing_fg_files = fileids_per_novel_classes[id_cls]
    #         available_bg = [img for img in dataset if img['image_id'] not in existing_fg_files]
    #         if len(available_bg) >= n_bg_rand:
    #             dicts['dataset'][id_cls].extend(random.sample(available_bg, n_bg_rand))
    #         else:
    #             print("not available")
    #             break
    #             #dicts['dataset'][id_cls].extend(available_bg)


    print("Total dataset: ", len(dataset))
    print("Total selected dataset: ", len(dicts['dataset']))
    #print("Total selected dataset for first class: ", len(dicts['dataset']))

    # Folder to save new data images
    Output_Images = os.path.join(FolderForGenVersion, f"JPEGImages_gen/{sid}") # datasets/coco/JPEGImages_gen/

    # Folder to save new data annotations
    Output_Annotations = os.path.join(FolderForGenVersion, f"Annotations_gen/{sid}") # datasets/coco/Annotations_gen/

    # Save information of generation process
    Log_Image_Path = os.path.join(FolderForGenVersion, "LogImagePath.txt") # datasets/coco/LogImagePath/

    os.makedirs(Output_Images, exist_ok=True)
    os.makedirs(Output_Annotations, exist_ok=True)

    dicts['Output_Images'] = Output_Images
    dicts['Output_Annotations'] = Output_Annotations
    dicts['Log_Image_Path'] = Log_Image_Path
    dicts['novel_classes'] = novel_classes

    # if dicts['background_clutter']['use']:
    #     base_entropy = torch.cat(base_entropy, dim=0)
    #     print('base_entropy.shape of background_similarity: ', base_entropy.shape)
    #
    #     indx = torch.argsort(base_entropy, descending=True).tolist()
    #     dataset_clutter = [dataset[i] for i in indx][:int(max_num_novel_ins * len(novel_classes) * 2)]
    #
    #     for id_cls in range(num_novel_classes):
    #         dicts['dataset'][id_cls].extend(
    #             random.sample(dataset_clutter, int(max_num_novel_ins * general_p_bg))
    #         )
    #
    # if dicts['background_similarity']['use']:
    #     base_feature = torch.cat(base_feature, dim=0).cuda()
    #     print('base_feature.shape of background_similarity: ', base_feature.shape)
    #
    #     for id_cls, novel_cls in enumerate(novel_classes):
    #         syn_novel_feature = torch.load(os.path.join(feature_dir, coco2voc.get(novel_cls, novel_cls) + "_tensor.pt"))
    #         syn_novel_feature = get_features(syn_novel_feature, in_features=in_features).cuda()
    #         Mean_Novel_Features = torch.mean(syn_novel_feature, dim=0, keepdims=True)
    #         cos = torch.nn.CosineSimilarity(dim=1)
    #
    #         score_similarity = cos(Mean_Novel_Features, base_feature)
    #         indx = torch.argsort(score_similarity, descending=True).tolist()
    #
    #         dataset_similar = [dataset[i] for i in indx][:int(max_num_novel_ins * general_p_bg)]
    #
    #         dicts['dataset'][id_cls].extend(dataset_similar)
    # DUMP
    # out = Path("dict.json")
    # with out.open("w", encoding="utf-8") as f:
    #     json.dump(dicts, f, ensure_ascii=False, indent=2)
    # exit()
    main(dicts)