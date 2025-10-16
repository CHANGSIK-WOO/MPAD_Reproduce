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

    # id2name, name2id = {}, {}
    # if is_coco:
    #     id2name = {i['id']: i['name'] for i in COCO_CATEGORIES}
    #     name2id = {i['name']: i['id'] for i in COCO_CATEGORIES}

    list_novel_classes = []
    global_dataset = []

    for sub_data, novel_cls in zip(dicts['dataset'], novel_classes):
        global_dataset.extend(sub_data)
        list_novel_classes.extend([novel_cls] * len(sub_data))

    dataloader = DataLoader(CustomImageDataset(global_dataset),
                            batch_size=batch_size, shuffle=False,
                            sampler=DistributedSampler(global_dataset))

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
            eddited_images, _ = torch_edit(painter, images, masks, Prompt_A, Prompt_B,
                                           mix_up_alpha=mix_up_alpha, num_inference_steps=NUM_INFERENCE_STEP,
                                           momemtum=momemtum)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            continue

        if not eddited_images[0]:
            continue

        for i in range(len(dict_input_data)):
            New_Index += 1
            result_pil = eddited_images[i]
            mask = unresized_masks[i]
            original_shape = shape[i]
            pA = Prompt_A[i]
            pB = Prompt_B[i]
            original_image_pil = pil_images[i]
            size = original_image_pil.size
            output_image = result_pil.resize(size)
            f_name = dict_input_data[i]['file_name'].split('/')[-1].split('.')[0]

            image_name = f"syn{f_name}_{New_Index:08d}.jpg"
            New_Index_Img = int(str(dict_input_data[i]['image_id']) + str(New_Index))
            process_obj = [class_B[i], class_A[i], expanded_bbox[i]]
            iter_process = choiced_index_list[i]
            output_image.save(Output_Images + image_name)

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

                ET.ElementTree(root).write(Output_Annotations + image_name.replace(".jpg", ".xml"),
                                           encoding='utf-8', xml_declaration=False)
                Log_Edited_Image[New_Index] = pA + "_" + pB + image_path_list[i]
                # # handle coco annotation saving here
                # for iter_annotation, old_obj in enumerate(dict_input_data[i]['annotations']):
                #     obj = deepcopy(old_obj)
                #     o_bbox = process_obj[2]  # Get bounding box
                #
                #     if iter_process == iter_annotation:
                #         final_bbox = convert_bbox_xyxy_to_xywh(o_bbox)
                #
                #         category_ids = [name2id[voc2coco.get(process_obj[0], process_obj[0])], \
                #                         name2id[
                #                             voc2coco.get(process_obj[1], process_obj[1])]]  # Set name of new classes
                #         if check_negative_bbox(final_bbox):
                #             continue
                #
                #         saved_annotations.append({
                #             "id": int('98' + str(obj['id']) + str(New_Index)),
                #             "image_id": New_Index_Img,
                #             "iscrowd": False,
                #             "bbox": final_bbox,
                #             "category_id": category_ids[-1],
                #             "all_category_id": ' '.join(map(str, category_ids)),
                #             "pA": pA,
                #             "pB": pB,
                #             "pname": id2name[obj['category_id']],
                #         })
                #     elif not check_iou(o_bbox, obj['bbox']):
                #         obj.update({
                #             "image_id": New_Index_Img,
                #             "id": int(str(obj['id']) + str(New_Index)),
                #             "bbox": convert_bbox_xyxy_to_xywh(obj['bbox'])
                #         })
                #         saved_annotations.append(obj)
                # saved_images.append({
                #     'id': New_Index_Img,
                #     'file_name': image_name,
                #     'width': output_image.size[0],
                #     'height': output_image.size[1],
                # })
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

                ET.ElementTree(root).write(Output_Annotations + image_name.replace(".jpg", ".xml"),
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
    parser.add_argument("--sid", type=int, default=1)
    parser.add_argument("--coco", action="store_true")
    parser.add_argument("--num-fine-grained", type=int, default=4,
                        help="The number of fine-grained classes per novel class")

    return parser


def get_features(features, in_features=['res2', 'res3']):
    return torch.cat([features[f] for f in in_features], dim=1)


def main(dicts):
    world_size = torch.cuda.device_count()

    with torch.no_grad():
        mp.spawn(run_inference_background, args=(world_size, dicts,), nprocs=world_size, join=True)

    # Save image log to be eddited
    with open(Log_Image_Path, 'w+') as file:
        for key, value in Log_Edited_Image.items():
            file.write(f"{key}: {value}\n")


if __name__ == "__main__":

    args = default_argument_parser().parse_args()
    print('args: ', args)

    FolderForGenVersion = args.gendata_folder
    max_num_novel_ins = args.num_ins

    VOC_DATASET = [
        (0, 'voc_2007_trainval', "VOC2007", "trainval"),
        (1, 'voc_2012_trainval', "VOC2012", "trainval"),
    ]
    #COCO_DATASET = ("coco14_trainval_base", "coco/trainval2014", "cocosplit/datasplit/trainvalno5k.json")
    # (id_dataset, name, dirname, split)
    COCO_DATASET = [
        (1, 'FS_OWODB', "coco", "t1"),
        (2, 'FS_OWODB', "coco", "t2"),
        (3, 'FS_OWODB', "coco", "t3"),
        (4, 'FS_OWODB', "coco", "t4"),
    ]

    dicts = {}

    general_p_bg = 1 / max(args.bg_sim + args.bg_clutter + args.bg_rand, 1)
    general_p_fg = 1 / max(args.fg_fg + args.fg_rand, 1)

    sid = args.sid
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

    # novel_classes = None
    # base_classes = None
    num_remove = 0
    is_coco = args.coco

    dataset = []
    choose_ids = []
    base_feature = []
    base_entropy = []
    removed_id_list = []
    in_features = ['res2', 'res3', 'res4', 'res5']

    if is_coco:

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

            # Name_Base = "Base_all_{}_{}_tensor_vit.pt"
            # # Name_Base = "Base_all_{}_{}_tensor_resnet.pt" # resnet101
            # # Name_Base = "Base_all_{}_{}_tensor_resnet50.pt"
            # entropy = torch.load(os.path.join(feature_dir, Name_Base.format('entropy', dirname.lower())))[choose_id]
            #
            # Name_Base = "Base_all_{}_{}_tensor.pt"
            # print(os.path.join(feature_dir, Name_Base.format('feature', dirname.lower())))
            # feature = torch.load(os.path.join(feature_dir, Name_Base.format('feature', dirname.lower())))
            #
            # feature = get_features(feature, in_features=in_features)[choose_id]
            # base_feature.append(feature)
            # base_entropy.append(entropy)

            dataset.extend(data)
            print('loaded {} with {} images, removed {}, take {:0.5f}s:'.format(name, len(data), len(removed_id),
                                                                                time() - tic))

        # novel_classes = [
        #     k["name"] for k in COCO_NOVEL_CATEGORIES if k["isthing"] == 1
        # ]
        #
        # base_classes = [
        #     k for k in COCO_CATEGORIES if k["isthing"] == 1 and k["name"] not in novel_classes
        # ]
        # name, dirname, json = COCO_DATASET
        # dataset, choose_id = load_coco_json(os.path.join(dataset_path, json), \
        #                                     os.path.join(dataset_path, dirname), COCO_NOVEL_CATEGORIES,
        #                                     max_instance=None)
        #
        # name = 'coco'
        # Name_Base = "Base_{}_{}_tensor.pt"  # 5000
        # Name_Base = "Base_all_{}_{}_tensor.pt"
        #
        # feature = torch.load(os.path.join(feature_dir, Name_Base.format('feature', name.lower())))
        # entropy = torch.load(os.path.join(feature_dir, Name_Base.format('entropy', name.lower())))
        #
        # feature = get_features(feature, in_features=in_features)
        # base_feature.append(feature)
        # base_entropy.append(entropy)

    else:
        novel_classes = PASCAL_VOC_NOVEL_CATEGORIES[sid]
        base_classes = PASCAL_VOC_BASE_CATEGORIES[sid]
        # dicts['meta_VOC_info'] = {1: meta_VOC_info_1,
        #                 2: meta_VOC_info_2,
        #                 3: meta_VOC_info_3}[sid]

        for id_dataset, name, dirname, split in VOC_DATASET:
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
            print('loaded {} with {} images, removed {}, take {:0.5f}s:'.format(name, len(data), len(removed_id),
                                                                                time() - tic))

    num_novel_classes = len(novel_classes)
    dicts['dataset'] = [[] for _ in range(num_novel_classes)]

    if args.bg_rand:
        n_bg_rand = int(max_num_novel_ins * general_p_bg)
        for id_cls in range(num_novel_classes):
            dicts['dataset'][id_cls].extend(dataset[id_cls * n_bg_rand:(id_cls + 1) * n_bg_rand])

    print("Total dataset: ", len(dataset))
    print("Total selected dataset: ", len(dicts['dataset']))
    print("Total selected dataset for first class: ", len(dicts['dataset'][0]))

    # Folder to save new data images
    Output_Images = os.path.join(FolderForGenVersion, "JPEGImages_gen/")

    # Folder to save new data annotations
    Output_Annotations = os.path.join(FolderForGenVersion, "Annotations_gen/")

    # Save information of generation process
    Log_Image_Path = os.path.join(FolderForGenVersion, "LogImagePath.txt")

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
    main(dicts)