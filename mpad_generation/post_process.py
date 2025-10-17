# utils/cleaned_dataset_utils.py

import os
import shutil
import sys
import numpy as np
from PIL import Image
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from copy import copy, deepcopy
import torch
import cv2

from utils.metadata import (
    PASCAL_VOC_NOVEL_CATEGORIES, 
    PASCAL_VOC_BASE_CATEGORIES,
    COCO_NOVEL_CATEGORIES,
    COCO_BASE_CATEGORIES,
    COCO_CATEGORIES,
)
from utils.functions import *

def merge_file(scr_path, dir_path):
    files = next(os.walk(scr_path))[2]
    for file in files:
        shutil.copy(os.path.join(scr_path, file), os.path.join(dir_path, file))
    return files

def _to_int(s):
    # '45.7' 같은 문자열도 안전하게 int로
    try:
        return int(s)
    except ValueError:
        return int(float(s))

def get_simple_input_information(xml_path, image_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    input_image = Image.open(image_path)

    bboxes, classes = [], []
    for obj in root.findall("object"):
        cls_name = obj.find("name").text
        bndbox = obj.find("bndbox")
        xmin, ymin = _to_int(bndbox.find('xmin').text), _to_int(bndbox.find('ymin').text)
        xmax, ymax = _to_int(bndbox.find('xmax').text), _to_int(bndbox.find('ymax').text)
        classes.append(cls_name)
        bboxes.append([xmin, ymin, xmax, ymax])

    size_node = root.find("size")
    width = int(size_node.find("width").text)
    height = int(size_node.find("height").text)

    return input_image, bboxes, width, height, classes

def filter_bbox_voc(anno_file, novel_classes, alpha=0.5):
    root = ET.parse(anno_file).getroot()
    boxes, class_names = [], []
    novel_ins_id, rm_cnt = None, 0

    for i, obj in enumerate(root.findall("object")):
        cls_name = obj.find("name").text
        bndbox = obj.find("bndbox")
        box = [int(bndbox.find(coord).text) for coord in ['xmin', 'ymin', 'xmax', 'ymax']]
        class_names.append(cls_name)
        boxes.append(box)
        if cls_name in novel_classes or cls_name.split("_")[-1] in novel_classes:
            novel_ins_id = i

    for j, obj in enumerate(root.findall("object")):
        if novel_ins_id != j and check_iou(boxes[novel_ins_id], boxes[j], alpha=alpha):
            root.remove(obj)
            rm_cnt += 1
    return rm_cnt

def remove_file(dataset_path, name):
    annotation_path = os.path.join(dataset_path, 'Annotations', f'{name}.xml')
    image_path = os.path.join(dataset_path, 'JPEGImages', f'{name}.jpg')

    if not os.path.isfile(annotation_path):
        print('Missing XML:', annotation_path)
        return True

    image, bboxes, width, height, _ = get_simple_input_information(annotation_path, image_path)

    # if any(check_pixels_black(np.asarray(image), downscale(box, 4)) for box in bboxes):
    #     print('Generate black pixels:', image_path)
    #     return True

    if (width, height) != image.size:
        print('Inconsistent dimensions:', image_path)
        return True

    return False

def remove_black_images_in_coco(image_root, dataset, datasetname, num_max_ins):
    images = dataset['images']
    annotations = dataset['annotations']
    
    images = {image['id']:image for image in images}
    tempt = defaultdict(list)
    for anno in annotations:
        tempt[anno['image_id']].append(anno)
    annotations = tempt
    img_ids = list(images.keys())
    
    num_files = len(images)
    print('len annotations: ', len(annotations))

    id2class = {i['id']:i['name'] for i in COCO_NOVEL_CATEGORIES}
    saved_files = list(img_ids)
    tempt_images = []
    
    for img_id in img_ids:

        image = images[img_id]
        anno  = annotations[img_id]
        novel_ins_id = None
        bboxes = []
        classnames = []

        for ins_id, obj in enumerate(anno):
            if isinstance(obj['category_id'], str):
                class_id = [int(i) for i in obj['category_id'].split(' ')][-1]
            else:
                class_id = [obj['category_id'], obj['category_id']][-1]

            if class_id in list(id2class.keys()):
                novel_ins_id = ins_id
                class_id_novel = class_id
            bboxes.append(convert_bbox_xywh_to_xyxy(obj['bbox']))
            classnames.append(id2class.get(class_id, class_id))

    
    temp_anno = {}
    temp_annotations = []
    print('num_max_ins', num_max_ins)
    for obj in dataset['annotations']:
        if isinstance(obj['category_id'], str):
            class_id = [int(i) for i in obj['category_id'].split(' ')][-1]
        else:
            class_id = [obj['category_id'], obj['category_id']][-1]
        cnt = temp_anno.get(class_id, 0)
        cnt += 1 
        if cnt < num_max_ins:
            temp_anno[class_id] = cnt
            temp_annotations.append(obj)

    stas = []
    for obj in temp_annotations:
        if obj['image_id'] not in saved_files: continue
        if isinstance(obj['category_id'], str):
            class_id = [int(i) for i in obj['category_id'].split(' ')][-1]
        else:
            class_id = [obj['category_id'], obj['category_id']][-1]
        if class_id in id2class.keys():
            stas.append( id2class[class_id] )

    print('global_classes', Counter(stas))
    print('sum Counter(stas)', sum(Counter(stas).values()))

    print('There are {} files, remained {} files, removed {} files'.format(
        num_files, len(saved_files), num_files-len(saved_files)))
    
    clean_dataset = copy(dataset)
    clean_dataset['annotations'] = temp_annotations

    return clean_dataset


def visualizer(img_path, novel_id, bboxes, classnames):
    # Read the image
    if isinstance(img_path , list):
        o_img = cv2.imread(img_path[0])
        img = cv2.imread(img_path[1])
    else:
        img = cv2.imread(img_path)
    # Convert the image to RGB (OpenCV reads in BGR format)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Iterate through the bounding boxes and class names
    for idx, (bbox, classname) in enumerate(zip(bboxes, classnames)):
        # Set the color: red for novel_id, green otherwise
        color = (255, 0, 0) if idx == novel_id else (0, 255, 0)
        
        # Unpack the bounding box coordinates
        bbox = [int(i) for i in bbox]
        x1, y1, x2, y2 = bbox
        
        # Draw the rectangle around the detected object
        img_rgb = cv2.rectangle(img_rgb, (x1, y1), (x2, y2), color, 2)
        
        # Put the class name above the rectangle
        cv2.putText(img_rgb, str(classname), (x1+5, y1 + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    
    # Save the image using OpenCV (convert back to BGR format for saving)
    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    
    if isinstance(img_path , list):

        width = min(o_img.shape[1], img_bgr.shape[1])
        o_img = cv2.resize(o_img, (width, int(o_img.shape[0] * width / o_img.shape[1])))
        img_bgr = cv2.resize(img_bgr, (width, int(img_bgr.shape[0] * width / img_bgr.shape[1])))
    
        # Concatenate images vertically
        img_bgr = np.vstack((o_img, img_bgr))
    return img_bgr

def remove_black_images_in_coco(image_root, dataset, datasetname, num_max_ins):
    
    # dataset = torch.load(annotation_file)
    images = dataset['images']
    annotations = dataset['annotations']
    
    images = {image['id']:image for image in images}
    tempt = defaultdict(list)
    for anno in annotations:
        tempt[anno['image_id']].append(anno)
    annotations = tempt
    img_ids = list(images.keys())
    
    num_files = len(images)
    print('len annotations: ', len(annotations))

    id2class = {i['id']:i['name'] for i in COCO_NOVEL_CATEGORIES}
    saved_files = list(img_ids)
    tempt_images = []
    cnt = -10 
    for img_id in img_ids:

        image = images[img_id]
        anno  = annotations[img_id]
        # print(len(anno))

        # bboxes = [[int(j) for j in i['bbox']] for i in anno]
        
        novel_ins_id = None
        bboxes = []
        classnames = []

        for ins_id, obj in enumerate(anno):
            if isinstance(obj['category_id'], str):
                class_id = [int(i) for i in obj['category_id'].split(' ')][-1]
            else:
                class_id = [obj['category_id'], obj['category_id']][-1]
            
            # x, y, w, h = [int(i) for i in obj['bbox']]

            if class_id in list(id2class.keys()):
                novel_ins_id = ins_id
                class_id_novel = class_id
            bboxes.append(convert_bbox_xywh_to_xyxy(obj['bbox']))
            classnames.append(id2class.get(class_id, class_id))

        # if check_negative_bbox(anno):
        # if any([[int(i) for i in obj['bbox']] for obj in anno])
            # print([[int(i) for i in obj['bbox']] for obj in anno])
            # print(bboxes)
            # saved_files.remove(img_id)

            # {"color": [220, 20, 60], "isthing": 1, "id": 1, "name": "person"},
            # {"color": [119, 11, 32], "isthing": 1, "id": 2, "name": "bicycle"},
            # {"color": [0, 0, 142], "isthing": 1, "id": 3, "nkhoaame": "car"},
            # {"color": [0, 0, 230], "isthing": 1, "id": 4, "name": "motorcycle"},
            # {"color": [106, 0, 228], "isthing": 1, "id": 5, "name": "airplane"},
            # {"color": [0, 60, 100], "isthing": 1, "id": 6, "name": "bus"},
            # {"color": [0, 80, 100], "isthing": 1, "id": 7, "name": "train"},
            # {"color": [0, 0, 192], "isthing": 1, "id": 9, "name": "boat"},
            # {"color": [165, 42, 42], "isthing": 1, "id": 16, "name": "bird"},
            # {"color": [255, 77, 255], "isthing": 1, "id": 17, "name": "cat"},
            # {"color": [0, 226, 252], "isthing": 1, "id": 18, "name": "dog"},
            # {"color": [182, 182, 255], "isthing": 1, "id": 19, "name": "horse"},
            # {"color": [0, 82, 0], "isthing": 1, "id": 20, "name": "sheep"},
            # {"color": [120, 166, 157], "isthing": 1, "id": 21, "name": "cow"},
            # {"color": [197, 226, 255], "isthing": 1, "id": 44, "name": "bottle"},
            # {"color": [153, 69, 1], "isthing": 1, "id": 62, "name": "chair"},
            # {"color": [3, 95, 161], "isthing": 1, "id": 63, "name": "couch"},
            # {"color": [163, 255, 0], "isthing": 1, "id": 64, "name": "potted plant"},
            # {"color": [0, 182, 199], "isthing": 1, "id": 67, "name": "dining table"},
            # {"color": [183, 130, 88], "isthing": 1, "id": 72, "name": "tv"},

        img_name = image['file_name']
        if cnt < 0:
            # print()
            PATH="../../khoanva/MPAD_train/DeFRCN/datasets/"
            datasetname='COCOGen_novel'
            img_path=PATH+f'{datasetname}/JPEGImages/'+img_name
            # print(obj['bbox'])
            # print('img_name', img_path)
            origin_img_path=PATH+'coco/trainval2014/COCO_'+'_'.join(img_name.split("_")[1:-1])+'.jpg'
            # print(origin_img_path)
            tempt_images.append(visualizer([origin_img_path, img_path], novel_ins_id, bboxes, classnames))
            # tempt_images.append(visualizer(img_path, novel_ins_id, bboxes, classnames))
            # assert 0
            # continue
            # break
            cnt += 1


    
        
        # # bbox = 
        # for ins_id in range(len(bboxes)):
        #     if novel_ins_id != ins_id \
        #         and Check_IOU(bboxes[novel_ins_id], bboxes[ins_id]) \
        #         and img_id in saved_files:
        #         saved_files.remove( img_id )
    if len(tempt_images) > 0:
        # print([type(i) for i in tempt_images])
        max_height = max([image.shape[0] for image in tempt_images])#/len(tempt_images)
        # print("max_height", max_height)
        # Resize all images to have the same height
        # resized_images = [cv2.resize(img, (int(img.shape[1] * min_height / img.shape[0]), min_height)) for img in tempt_images]

        # Resize all images to have the maximum height
        resized_images = [cv2.resize(img, (int(img.shape[1] * max_height / img.shape[0]), max_height)) for img in tempt_images]

        # Concatenate images horizontally
        concatenated_img = np.hstack(resized_images)
        print('save tempt.png image')
        # Save the concatenated image
        cv2.imwrite("tempt.png", concatenated_img)
    
    temp_anno = {}
    temp_annotations = []
    print('num_max_ins', num_max_ins)
    for obj in dataset['annotations']:
        if isinstance(obj['category_id'], str):
            class_id = [int(i) for i in obj['category_id'].split(' ')][-1]
        else:
            class_id = [obj['category_id'], obj['category_id']][-1]
        cnt = temp_anno.get(class_id, 0)
        cnt += 1 
        if cnt < num_max_ins:
            temp_anno[class_id] = cnt
            temp_annotations.append(obj)

    # print("temp_anno", temp_anno)
    # temp_annotations = []
    stas = []
    # for obj in dataset['annotations']:
    for obj in temp_annotations:
        if obj['image_id'] not in saved_files: continue
        # temp_annotations.append(obj)
        if isinstance(obj['category_id'], str):
            class_id = [int(i) for i in obj['category_id'].split(' ')][-1]
        else:
            class_id = [obj['category_id'], obj['category_id']][-1]
        if class_id in id2class.keys():
            stas.append( id2class[class_id] )

    print('global_classes', Counter(stas))
    print('sum Counter(stas)', sum(Counter(stas).values()))
    # print(len(new_files))
    # saved_files = get_k_sample(
    #     dataset_path, saved_files, novel_classes, num_max_ins)

    print('There are {} files, remained {} files, removed {} files'.format(
        num_files, len(saved_files), num_files-len(saved_files)))
    
    # with open(file_path, 'w+') as f:
    #     f.write('\n'.join(saved_files))
    # print('Saved to set_dir: ' + file_path)

    clean_dataset = copy(dataset)
    clean_dataset['annotations'] = temp_annotations

    return clean_dataset


def get_k_sample(dataset_path, list_files, novel_classes, num_max_ins):
    annotation_dir = os.path.join(dataset_path, 'Annotations')
    sample_counts = {cls: 0 for cls in novel_classes}
    selected, global_classes = [], []

    for name in list_files:
        xml_path = os.path.join(annotation_dir, f'{name}.xml')
        img_path = os.path.join(dataset_path, 'JPEGImages', f'{name}.jpg')
        _, _, _, _, classes = get_simple_input_information(xml_path, img_path)
        global_classes.extend(classes)

        for cls in classes:
            cls_base = cls.split('_')[-1] if '_' in cls else cls
            if cls_base in novel_classes and sample_counts[cls_base] < num_max_ins:
                sample_counts[cls_base] += 1
                selected.append(name)
                break

    print(sample_counts)
    return selected

def create_meta_infor(dataset_path, novel_classes, num_max_ins):
    set_dir = os.path.join(dataset_path, 'ImageSets/Main')
    annotation_dir = os.path.join(dataset_path, 'Annotations_gen')
    os.makedirs(set_dir, exist_ok=True)

    image_files = [f.split('.')[0] for f in os.listdir(os.path.join(dataset_path, 'JPEGImages')) if f.endswith('.jpg')] + [f.split('.')[0] for f in os.listdir(os.path.join(dataset_path, 'JPEGImages_gen')) if f.endswith('.jpg')]
    all_files = set(image_files)
    num_files = len(all_files)

    remove_list = [f for f in all_files if remove_file(dataset_path, f)]
    # print(remove_list)
    rm_cnt = [
        filter_bbox_voc(os.path.join(annotation_dir, f"{file}.xml"), novel_classes, alpha=0.7)
        for file in all_files
    ]
    print(sum(rm_cnt))
    # print(rm_cnt)
    saved_files = [file for i, file in enumerate(all_files) if file not in remove_list and rm_cnt[i] == 0]
    saved_files = get_k_sample(dataset_path, saved_files, novel_classes, num_max_ins)
    # saved_files = list(all_files)
    print(
        f'There are {num_files} files, remained {len(saved_files)} files, removed {num_files - len(saved_files)} files')

    file_path = os.path.join(set_dir, 'train.txt')
    with open(file_path, 'w') as f:
        f.write('\n'.join(saved_files))
    print('Saved to set_dir:', file_path)

def remove_file_coco(image_root, image, bboxes):
    img_path = os.path.join(image_root, image['file_name'])
    input_image = Image.open(img_path)

    if any(check_pixels_black(input_image, box) for box in bboxes):
        return True

    if (image['width'], image['height']) != input_image.size:
        print('Inconsistent dimensions:', img_path)
        return True

    return False

def main(argv):
    dataset_path = argv[1]
    num_max_ins = int(argv[3])

    sid = int(argv[2])
    novel_classes = COCO_NOVEL_CATEGORIES[sid]
    create_meta_infor(dataset_path, novel_classes, num_max_ins)

    # if 'coco' in dataset_path.lower():
    #     image_root = os.path.join(dataset_path, "JPEGImages")
    #     annotation_file = os.path.join(dataset_path, "Annotations/data.pt")
    #     synthesis_dataset = {"images": [], "annotations": []}
    #
    #     for rank in range(8):
    #         path = os.path.join(dataset_path, f'Annotations/data_{rank}.pt')
    #         if os.path.exists(path):
    #             temp_data = torch.load(path, map_location='cpu')
    #             synthesis_dataset["images"].extend(temp_data["images"])
    #             synthesis_dataset["annotations"].extend(temp_data["annotations"])
    #
    #     synthesis_dataset = remove_black_images_in_coco(image_root, synthesis_dataset, dataset_path, num_max_ins)
    #     torch.save(synthesis_dataset, annotation_file)
    # else:
    #     sid = int(argv[2])
    #     novel_classes = PASCAL_VOC_NOVEL_CATEGORIES[sid]
    #     create_meta_infor(dataset_path, novel_classes, num_max_ins)

if __name__ == "__main__":
    main(sys.argv)
