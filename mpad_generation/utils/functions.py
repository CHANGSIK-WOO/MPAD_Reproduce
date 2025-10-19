import os
import json
import random
import io
from typing import Any, Dict, List, Optional, Tuple, Union
from copy import copy, deepcopy

import torch
import numpy as np
import cv2 as cv
import torchvision
from torchvision.transforms import functional as TF

from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import xml.etree.ElementTree as ET
# from diffusers.utils import USE_PEFT_BACKEND, BaseOutput, load_image
import contextlib
from torch.distributed import init_process_group

device_dtype = torch.float32 if torch.cuda.is_available() else torch.float32
KERNEL = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3, 3))
DILATE_KERNEL = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
TENSOR_KERNEL = torch.tensor(KERNEL, dtype=device_dtype)[None, None, ...]
TENSOR_DILATE_KERNEL = torch.tensor(DILATE_KERNEL, dtype=device_dtype)[None, None,...]

def torch_erosion(im_tensor, kernel):
    return 1 - torch.clamp(torch.nn.functional.conv2d(1 - im_tensor, kernel, padding='same'), 0, 1)

def torch_dilation(im_tensor, kernel):
    return torch.clamp(torch.nn.functional.conv2d(im_tensor, kernel, padding='same'), 0, 1)

def torch_open(im_tensor, kernel):
    return torch_dilation(torch_erosion(im_tensor, kernel), kernel)

def ddp_setup(rank: int, world_size: int):
    """
    Args:
        rank: Unique identifier of each process
        world_size: Total number of processes
    """
    os.environ["MASTER_ADDR"] = os.getenv("MASTER_ADDR", "localhost")
    os.environ["MASTER_PORT"] = os.getenv("MASTER_PORT", "12355")  # 환경변수 우선
    torch.cuda.set_device(rank)
    init_process_group(backend="nccl", rank=rank, world_size=world_size)

def preprocess2(image_path_list, annotations, augment_multi_scale=False, p_multi_scale=0.5):
    
    images = []
    choiced_index_list = []
    labels = []
    pil_images = []

    for i, ins in zip(image_path_list, annotations):
        pil_image = Image.open(i).convert('RGB')
        images.append(pil_image)
        # choose first instance in annatations of the image
        choiced_index =  0 
        choiced_index_list.append(choiced_index)
        labels.append(ins[choiced_index])
        pil_images.append(pil_image)
    
    shape = torch.tensor([[i.size[0] for i in images], [i.size[1] for i in images]]).T # list(W, H)
    
    W = torch.max(shape[:, 0]).detach()
    H = torch.max(shape[:, 1]).detach()
    if H < W:
        H, W = 640, int(W / H * 640)
    else:
        H, W = int(H / W * 640), 640
    W = int(W - W % 8)
    H = int(H - H % 8)

    temp_images = []


    # list_bbox = [ins['bbox'] for ins in labels]
    dilation_pixels = 3 * 2  # Kernel size multiplied by number of iterations
    list_bbox = []
    expanded_bbox= []
    for i, ins in enumerate(labels):

        new_box = ins['bbox'] # xyxy
        if  augment_multi_scale and random.uniform(0, 1) < p_multi_scale:
            new_box = expand_bounding_box(new_box)

        
        temp_bbox = [max(new_box[0] - dilation_pixels,0),  # x1
            max(new_box[1] - dilation_pixels, 0),  # y1
            min(new_box[2] + dilation_pixels, shape[i][0]),  # x2
            min(new_box[3] + dilation_pixels, shape[i][1])   # y2
        ]

        temp_bbox = [int(i) for i in temp_bbox]
        expanded_bbox.append(temp_bbox)


    scale = torch.tensor([H, W])/shape
    temp_bbox = deepcopy(expanded_bbox)
    resized_list_bbox = []
    for img, shape_, ins, box in zip(images, shape, labels, temp_bbox):
        image = torch.tensor(np.asarray(img.resize([W, H]))[None, ...], dtype=torch.float32)
        temp_images.append(image)

        # convert bbox to new relative shape to resize
        out_box = convert_box(box, [shape_[1], shape_[0]], type_in='XYXY_ABS', type_out='XYWH_REL')
        out_box = convert_box(out_box, [H, W], type_in='XYWH_REL', type_out='XYXY_ABS')
        
        
        resized_list_bbox.append([int(i) for i in out_box])

    images = torch.cat(temp_images, dim=0)
    images = torch.permute(images, [0, 3, 1, 2]) 
    masks = pytorch_masking(images, resized_list_bbox)

    unresized_masks = (masks.detach().clone().numpy()*255).astype(np.uint8)

    images = TF.resize(images, [H, W], antialias=False)
    masks = TF.resize(masks, [H, W], antialias=False)
    images = images / 127.5 - 1.0

    # print("expanded_bbox 2", expanded_bbox)
    # for i, ins in zip(image_path_list, annotations):
    #     images, masks
    # print(expanded_bbox)
    # print([annotations[i]['bbox'] for i in choiced_index_list])
    
    return {
        'images': images, 
        'masks': masks, 
        'unresized_masks': unresized_masks,
        'labels': labels, 
        'expanded_bbox': expanded_bbox, 
        'choiced_index_list': choiced_index_list,
        'pad_value': None,
        'shape': shape,
        'pil_images': pil_images,
        'pad_shape': (None, None),

    }

def downscale(bbox, scale=3):
    width = bbox[2] - bbox[0]   # xmax -xmin
    height = bbox[3] - bbox[1]   # ymax - ymin
    extend_width = int(width / scale)
    extend_height = int(height / scale)
    new_bbox = [
        bbox[0] + extend_width,
        bbox[1] + extend_height,
        bbox[2] - extend_width,
        bbox[3] - extend_height
    ]
    return new_bbox

def convert_bbox_xyxy_to_xywh(bbox):
    """
    Convert bounding box from XYXY_ABS mode to XYWH_ABS mode.
    
    Args:
    bbox (list or tuple): A bounding box in XYXY_ABS format [x_min, y_min, x_max, y_max]
    
    Returns:
    list: A bounding box in XYWH_ABS format [x, y, width, height]
    """
    x_min, y_min, x_max, y_max = bbox
    x = x_min
    y = y_min
    width = x_max - x_min
    height = y_max - y_min
    return [x, y, width, height]


def check_pixels_black(image, bbox):
    x_min, y_min, x_max, y_max = bbox
    # img = image.load()
    # img = np.asarray(img)
    # print(image.shape)
    pixels = image[x_min:x_max, y_min:y_max, :]
    # Kiểm tra xem mỗi kênh màu (RGB) có giá trị bằng 0 không
    if np.sum(pixels**2) == 0:
        return True
    return False

def convert_box(bbox, shape, type_in, type_out):
    assert type_in  in ['XYXY_ABS', 'XYWH_REL']
    assert type_out in ['XYXY_ABS', 'XYWH_REL']
    if type_in =='XYXY_ABS' and type_out =='XYWH_REL':
        h, w = shape
        bbox[2] -= bbox[0]
        bbox[3] -= bbox[1]

        bbox[0] /= w
        bbox[2] /= w
        bbox[1] /= h
        bbox[3] /= h
    else:
        h, w = shape
        bbox[0] *= w
        bbox[2] *= w
        bbox[1] *= h
        bbox[3] *= h

        bbox[2] += bbox[0]
        bbox[3] += bbox[1]
    return bbox

def check_iou(anchor_bbox, check_bbox, alpha=0.5):
    x1 = max(anchor_bbox[0], check_bbox[0])
    y1 = max(anchor_bbox[1], check_bbox[1])
    x2 = min(anchor_bbox[2], check_bbox[2])
    y2 = min(anchor_bbox[3], check_bbox[3])

    if x2 < x1:
        return False

    box2_area = (check_bbox[2] - check_bbox[0]) * (check_bbox[3] - check_bbox[1])
    union_area = (x2 - x1) * (y2 - y1)

    return union_area > box2_area * alpha

def check_negative_bbox(bbox):
    return any(i<0 for i in bbox)
    
def convert_bbox_xywh_to_xyxy(bbox):
    """
    Convert bounding box from XYXY_ABS mode to XYWH_ABS mode.
    
    Args:
    bbox (list or tuple): A bounding box in XYXY_ABS format [x_min, y_min, x_max, y_max]
    
    Returns:
    list: A bounding box in XYWH_ABS format [x, y, width, height]
    """
    x, y, w, h = bbox

    return [x, y, x+w, y+h]


# name: "FS-OWODB", dirname: "datasets/coco", split: "t1", classnames: "base_classes", max_instance: None
def load_filtered_voc_instances(
        name: str, dirname: str, split: str, classnames: str, max_instance: int
):
    """
    Load Pascal VOC detection annotations to Detectron2 format.
    Args:
        dirname: Contain "Annotations", "ImageSets", "JPEGImages"
        split (str): one of "train", "test", "val", "trainval"
    """
    #             data, removed_id, choose_id = load_filtered_voc_instances(name, os.path.join(dataset_path, dirname), split,
    #                                                                       base_classes,
    #                                                                       max_instance=None)  # choose base Images

    is_shots = "shot" in name
    if is_shots:
        fileids = {}
        shot = name.split("_")[-2].split("shot")[0]
        seed = int(name.split("_seed")[-1])
        split_dir = os.path.join(dirname, "vocsplit", "seed{}".format(seed))
        for cls in classnames:
            with open(
                    os.path.join(
                        split_dir, "box_{}shot_{}_train.txt".format(shot, cls)
                    )
            ) as f:
                fileids_ = np.loadtxt(f, dtype=str).tolist()
                if isinstance(fileids_, str):
                    fileids_ = [fileids_]
                fileids_ = [
                    fid.split("/")[-1].split(".jpg")[0] for fid in fileids_
                ]
                fileids[cls] = fileids_
    else:
        with open(os.path.join(dirname, "ImageSets","Main/t1" + ".txt")) as f: #datasets/coco/ImageSets/Main/t1.txt

            #print(f'os.path.join(dirname, "ImageSets", "Main", split + ".txt") : {os.path.join(dirname, "ImageSets", "Main", split + ".txt")}')
            fileids = np.loadtxt(f, dtype=str)
            # print(f"fileids : {fileids}, fileids length : {len(fileids)}")
    dicts = []
    removed_id = []
    choose_id = []

    if is_shots:
        dicts = {}
        for cls, fileids_ in fileids.items():
            dicts_ = []
            for fileid in fileids_:
               #year = "2012" if "_" in fileid else "2007"
               # anno_file = os.path.join(
               #     dirname, "VOC{}".format(year), "Annotations", fileid + ".xml"
               # )
               # jpeg_file = os.path.join(
               #     dirname, "VOC{}".format(year), "JPEGImages", fileid + ".jpg"
               # )
                anno_file = os.path.join(
                    dirname, "COCO", "Annotations", fileid + ".xml"
                )
                jpeg_file = os.path.join(
                    dirname, "COCO", "JPEGImages", fileid + ".jpg"
                )

                tree = ET.parse(anno_file)

                for obj in tree.findall("object"):
                    r = {
                        "file_name": jpeg_file,
                        "image_id": fileid,
                        "height": int(tree.findall("./size/height")[0].text),
                        "width": int(tree.findall("./size/width")[0].text),
                    }
                    cls_ = obj.find("name").text
                    if cls != cls_:
                        continue
                    bbox = obj.find("bndbox")
                    bbox = [
                        float(bbox.find(x).text)
                        for x in ["xmin", "ymin", "xmax", "ymax"]
                    ]
                    bbox[0] -= 1.0
                    bbox[1] -= 1.0

                    instances = [
                        {
                            "category_id": classnames.index(cls),
                            "classname": cls,
                            "bbox": bbox,
                            "bbox_mode": 'XYXY_ABS',
                            "iscrowd": 0,
                        }
                    ]
                    r["annotations"] = instances
                    dicts_.append(r)

            if len(dicts_) > int(shot):
                dicts_ = np.random.choice(dicts_, int(shot), replace=False)
            dicts[cls] = dicts_
            print(cls, ':', len(dicts_), end=' ')
        removed_id, choose_id = None, None
        print()
    else:
        for i, fileid in enumerate(fileids):
            anno_file = os.path.join(dirname, "Annotations", fileid + ".xml")
            jpeg_file = os.path.join(dirname, "JPEGImages", fileid + ".jpg")
            # print(f"anno_file : {anno_file}, jpeg_file : {jpeg_file}")

            tree = ET.parse(anno_file)

            r = {
                "file_name": jpeg_file,
                "anno_file": anno_file,
                "image_id": fileid,
                "height": int(tree.findall("./size/height")[0].text),
                "width": int(tree.findall("./size/width")[0].text),
            }
            #print(f"r : {r}")
            instances = []

            for obj in tree.findall("object"):
                cls = obj.find("name").text
                #print(f"cls : {cls}")
                #print(f"base_classnames : {classnames}, base_classnames length : {len(classnames)}")
                #print(cls in classnames)
                if not (cls in classnames): # cls is novel class
                    instances = []
                    #print("class not in classnames")
                    break

                # if cls is base class
                #print("cls is base class")
                bbox = obj.find("bndbox")
                bbox = [
                    int(bbox.find(x).text)
                    for x in ["xmin", "ymin", "xmax", "ymax"]
                ]
                bbox[0] -= 1
                bbox[1] -= 1
                #print(f"category_id : {classnames.index(cls)}, cls : {cls}, bbox : {bbox}")
                instances.append(
                    {
                        "category_id": classnames.index(cls),
                        "classname": cls,
                        "bbox": bbox,
                        "bbox_mode": 'XYXY_ABS',
                    }
                )
                #print(f"instances :{instances}")
            if len(instances) == 0:
                removed_id.append(i)
                continue
            r["annotations"] = instances
            choose_id.append(i)
            dicts.append(r)
            if max_instance and len(dicts) >= max_instance:
                return dicts, removed_id, choose_id
    return dicts, removed_id, choose_id

def load_coco_json(json_file, image_root, classnames, max_instance=5000):
    
    from pycocotools.coco import COCO
    with contextlib.redirect_stdout(io.StringIO()):
        coco_api = COCO(json_file)
    # sort indices for reproducible results
    classnames = [i['id'] for i in classnames]
    img_ids = sorted(list(coco_api.imgs.keys()))
    imgs = coco_api.loadImgs(img_ids)
    anns = [coco_api.imgToAnns[img_id] for img_id in img_ids]

    imgs_anns = list(zip(imgs, anns))
    
    dataset_dicts = []
    
    choose_id = []
    ann_keys = ["id", "iscrowd", "bbox", "category_id"]

    for i, (img_dict, anno_dict_list) in enumerate(imgs_anns):
        record = {}
        record["file_name"] = os.path.join(
            image_root, img_dict["file_name"]
        )
        record["height"] = img_dict["height"]
        record["width"] = img_dict["width"]
        image_id = record["image_id"] = img_dict["id"]

        objs = []
        for anno in anno_dict_list:
            assert anno["image_id"] == image_id
            assert anno.get("ignore", 0) == 0

            obj = {key: anno[key] for key in ann_keys if key in anno}

            obj["bbox_mode"] = "XYWH_ABS"                
            obj["image_id"] = image_id
            obj["bbox"] = convert_bbox_xywh_to_xyxy(obj["bbox"])

            if obj["category_id"] in classnames:
                objs = []
                break            
            obj["classname"] = obj["category_id"]
            objs.append(obj)

        if len(objs)==0: 
            continue

        record["annotations"] = objs
        if max_instance and len(dataset_dicts) >= max_instance:
            return dataset_dicts, choose_id
        choose_id.append(i)
        dataset_dicts.append(record)

    return dataset_dicts, choose_id

#POWER PAINT

def pytorch_masking(image: torch.Tensor, list_bbox: np.array):
    shape = image.shape

    if len(shape) == 4:
        b, _, h, w = shape
    else:
        _, h, w = shape
        b = 1
    
    kernel = TENSOR_KERNEL
    dilate_kernel = TENSOR_DILATE_KERNEL
    mask = torch.zeros((b, 1, h ,w), dtype=device_dtype)
    
    for i, bbox in enumerate(list_bbox):
        mask[i, :, bbox[1]: bbox[3], bbox[0]: bbox[2]] = 1.0

    mask = torch_open(mask, kernel)
    mask = torch_dilation(mask, dilate_kernel)
    mask = torch_dilation(mask, dilate_kernel)
    mask = torch_open(mask, kernel) # *255
    # Calculate the expanded bounding box
    return mask


def expand_bounding_box(bbox):
    x_min, y_min, x_max, y_max = bbox
    center_x = (x_min + x_max) // 2
    center_y = (y_min + y_max) // 2

    # Calculate the width and height of the original bounding box
    width = x_max - x_min
    height = y_max - y_min
    list_scale = [1.25, 1.5, 1.75, 2]
    # Calculate the new width and height after scaling
    scale = np.random.choice(list_scale,)
    # H_scale = random.choice(list_scale[:2])
    new_width = int(width * scale)
    new_height = int(height * scale)

    # Calculate the new top-left and bottom-right coordinates
    new_x_min = center_x - new_width  // 2
    new_y_min = center_y - new_height // 2
    new_x_max = center_x + new_width  // 2
    new_y_max = center_y + new_height // 2

    new_bbox = [new_x_min, new_y_min, new_x_max, new_y_max]
    return new_bbox

def torch_edit(painter, images: torch.Tensor, maskes: torch.Tensor, TARGET_PROMPT_A: str, TARGET_PROMPT_B:str, device: str='cuda', mix_up_alpha: int=0.7, num_inference_steps=80, momemtum=0.99):

    negative_template = 'blurry, unreal, disproportioned, dismembered, duplicate, deformed, malformed'
    
    TARGET_PROMPT_A = [A + ' P_obj' for A in TARGET_PROMPT_A]
    TARGET_PROMPT_B = [B + ' P_obj' for B in TARGET_PROMPT_B]
    NEG_PROMT_A     = [negative_template + ', multiple objects']*len(TARGET_PROMPT_A)
    NEG_PROMT_B     = NEG_PROMT_A

    _, _, H, W = images.shape
    seed = random.randint(0, 1000000)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    result = painter(
        promptA=TARGET_PROMPT_A,
        promptB=TARGET_PROMPT_B,
        tradoff=mix_up_alpha,
        tradoff_nag=0.5,  
        negative_promptA=NEG_PROMT_A,
        negative_promptB=NEG_PROMT_B,
        image=images,
        mask_image=maskes,
        width=W,
        height=H,
        guidance_scale=10, 
        num_inference_steps=num_inference_steps, 
        momemtum = momemtum,
        output_type='pil', 
    )[0].images
    return result, None
