#!/usr/bin/env python3
"""
MPAD 증강 통합 스크립트
- t1을 base class로, t2/t3/t4를 각각 novel class로 설정
- 각 novel class당 5개 이미지 선택, 각 이미지당 10개씩 증강
- 증강 결과를 JPEGImages_gen/{t2,t3,t4}/, Annotations_gen/{t2,t3,t4}/, ImageSets_gen/{t2,t3,t4}/에 저장
- 최종 매핑 JSON 생성
"""

import os
import sys
import json
import random
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict
import numpy as np

# Class definitions
VOC_CLASS_NAMES = [
    'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat',
    'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person',
    'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor'
]

T2_CLASS_NAMES = [
    'truck', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter',
    'bench', 'elephant', 'bear', 'zebra', 'giraffe',
    'backpack', 'umbrella', 'handbag', 'tie', 'suitcase',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator'
]

T3_CLASS_NAMES = [
    'frisbee', 'skis', 'snowboard', 'sports ball', 'kite',
    'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli',
    'carrot', 'hot dog', 'pizza', 'donut', 'cake'
]

T4_CLASS_NAMES = [
    'bed', 'toilet', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'book', 'clock',
    'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush',
    'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl'
]

# MS-COCO 전체 80 클래스 (인덱스 매핑용)
ALL_COCO_CLASSES = VOC_CLASS_NAMES + T2_CLASS_NAMES + T3_CLASS_NAMES + T4_CLASS_NAMES

STAGE_CONFIG = {
    't1': {
        'base_classes': [],  # t1은 base가 없음 (자체가 base)
        'novel_classes': VOC_CLASS_NAMES,
        'sid': 0,  # t1은 sid가 따로 없지만 0으로 설정
        'is_base': True
    },
    't2': {
        'base_classes': VOC_CLASS_NAMES,
        'novel_classes': T2_CLASS_NAMES,
        'sid': 1
    },
    't3': {
        'base_classes': VOC_CLASS_NAMES,
        'novel_classes': T3_CLASS_NAMES,
        'sid': 2
    },
    't4': {
        'base_classes': VOC_CLASS_NAMES,
        'novel_classes': T4_CLASS_NAMES,
        'sid': 3
    }
}

# Fine-tuning stage 설정 (누적)
FT_STAGE_CONFIG = {
    't2_ft': ['t1', 't2'],
    't3_ft': ['t1', 't2', 't3'],
    't4_ft': ['t1', 't2', 't3', 't4']
}


def select_images_per_class(dataset_path, stage, novel_classes, num_images=5, seed=42):
    """
    각 novel class별로 num_images개의 이미지를 선택

    Args:
        dataset_path: 데이터셋 경로 (예: "datasets/coco")
        stage: stage 이름 (t1, t2, t3, t4)
        novel_classes: novel class 리스트
        num_images: 각 클래스당 선택할 이미지 수
        seed: random seed

    Returns:
        dict: {class_name: [image_ids]}
    """
    random.seed(seed)

    # ImageSets/Main에서 stage 파일 읽기
    stage_file = os.path.join(dataset_path, "ImageSets", "Main", f"{stage}.txt")

    if not os.path.exists(stage_file):
        raise FileNotFoundError(f"Stage file not found: {stage_file}")

    with open(stage_file, 'r') as f:
        fileids = [line.strip() for line in f.readlines()]

    print(f"Loaded {len(fileids)} images from {stage_file}")

    # 각 클래스별로 이미지 분류
    class_to_images = {cls: [] for cls in novel_classes}

    for fileid in fileids:
        anno_file = os.path.join(dataset_path, "Annotations", f"{fileid}.xml")
        if not os.path.exists(anno_file):
            continue

        tree = ET.parse(anno_file)

        # 이미지에 포함된 클래스 확인
        classes_in_image = set()
        for obj in tree.findall("object"):
            cls_name = obj.find("name").text
            if cls_name in novel_classes:
                classes_in_image.add(cls_name)

        # 각 클래스에 이미지 추가
        for cls in classes_in_image:
            class_to_images[cls].append(fileid)

    # 각 클래스별로 num_images개 선택
    selected_images = {}
    for cls, images in class_to_images.items():
        if len(images) > num_images:
            selected_images[cls] = random.sample(images, num_images)
        else:
            selected_images[cls] = images
            if len(images) < num_images:
                print(f"Warning: {cls} has only {len(images)} images (requested {num_images})")

    return selected_images


def create_t1_sampled(dataset_path, num_images_per_class=15, seed=42):
    """
    ImageSets/Main/t1.txt에서 샘플링하여 Main_fewshot/t1_sampled.txt 생성
    VOC 20개 클래스에서 각 클래스당 num_images_per_class개씩 랜덤 선택

    Args:
        dataset_path: 데이터셋 경로 (예: "datasets/coco")
        num_images_per_class: 각 클래스당 선택할 이미지 수
        seed: random seed

    Returns:
        list: 선택된 image_ids
    """
    print(f"\n{'=' * 60}")
    print(f"Sampling t1: {num_images_per_class} images per class")
    print(f"{'=' * 60}\n")

    random.seed(seed)

    # ImageSets/Main/t1.txt에서 전체 이미지 목록 읽기
    t1_file = os.path.join(dataset_path, "ImageSets", "Main", "t1.txt")

    if not os.path.exists(t1_file):
        raise FileNotFoundError(f"t1.txt not found: {t1_file}")

    with open(t1_file, 'r') as f:
        all_fileids = [line.strip() for line in f.readlines()]

    print(f"Total available images in t1.txt: {len(all_fileids)}")

    # 각 클래스별로 이미지 분류
    class_to_images = {cls: [] for cls in VOC_CLASS_NAMES}

    for fileid in all_fileids:
        anno_file = os.path.join(dataset_path, "Annotations", f"{fileid}.xml")

        if not os.path.exists(anno_file):
            continue

        tree = ET.parse(anno_file)

        # 이미지에 포함된 클래스 확인
        classes_in_image = set()
        for obj in tree.findall("object"):
            cls_name = obj.find("name").text
            if cls_name in VOC_CLASS_NAMES:
                classes_in_image.add(cls_name)

        # 각 클래스에 이미지 추가
        for cls in classes_in_image:
            class_to_images[cls].append(fileid)

    # 각 클래스별로 num_images_per_class개 선택
    selected_fileids = set()
    for cls, images in class_to_images.items():
        images_unique = list(set(images))  # 중복 제거

        if len(images_unique) >= num_images_per_class:
            selected = random.sample(images_unique, num_images_per_class)
            selected_fileids.update(selected)
            print(f"{cls}: selected {len(selected)}/{len(images_unique)} images")
        else:
            selected_fileids.update(images_unique)
            print(f"{cls}: only {len(images_unique)} images available (requested {num_images_per_class})")

    # ImageSets/Main_fewshot/ 폴더 생성
    output_dir = os.path.join(dataset_path, "ImageSets", "Main_fewshot")
    os.makedirs(output_dir, exist_ok=True)

    # t1_sampled.txt 파일 저장
    t1_sampled_file = os.path.join(output_dir, "t1.txt")
    with open(t1_sampled_file, 'w') as f:
        for fileid in sorted(selected_fileids):
            f.write(f"{fileid}\n")

    print(f"\nTotal selected images: {len(selected_fileids)}")
    print(f"Saved to: {t1_sampled_file}")

    return list(selected_fileids)


def run_mpad_generation(dataset_path, stage, sid, selected_images, num_aug_per_image=10):
    """
    MPAD 증강 실행 - generate.sh의 내용을 Python으로 구현

    Args:
        dataset_path: 데이터셋 경로
        stage: stage 이름 (t2, t3, t4)
        sid: stage id (1, 2, 3)
        selected_images: {class_name: [image_ids]} 형태의 선택된 이미지 dict
        num_aug_per_image: 각 이미지당 증강 개수
    """
    print(f"\n{'=' * 60}")
    print(f"Running MPAD Generation for {stage.upper()}")
    print(f"{'=' * 60}\n")

    # ImageSet 파일 생성 - 선택된 이미지만 포함
    temp_imageset_dir = os.path.join(dataset_path, "ImageSets", "Main")
    os.makedirs(temp_imageset_dir, exist_ok=True)

    # 선택된 이미지 파일명 리스트
    selected_fileids = []
    for cls, imgs in selected_images.items():
        selected_fileids.extend(imgs)
    selected_fileids = sorted(set(selected_fileids))  # 중복 제거

    # 임시 stage 파일 생성
    temp_stage_file = os.path.join(temp_imageset_dir, f"{stage}_selected.txt")
    with open(temp_stage_file, 'w') as f:
        for fileid in selected_fileids:
            f.write(f"{fileid}\n")

    print(f"Created temporary stage file: {temp_stage_file}")
    print(f"Number of selected images: {len(selected_fileids)}")

    # generate.sh 명령 실행
    import subprocess

    # CUDA 디바이스 설정
    env = os.environ.copy()
    env['CUDA_VISIBLE_DEVICES'] = '0'

    cmd = [
        "python", "mpad_generation/main_generate_data.py",
        "--gendata-folder", dataset_path,
        "--sid", str(sid),
        "--num-ins", str(num_aug_per_image),
        "--bg-rand",
        "--bg-clutter",
        "--bg-sim",
        "--fg-rand",
        "--fg-fg",
        "--num-fine-grained", "4",
        "--fg-sim",
        "--p-fg-sim", "0.8",
        "--mix-up", "0.7",
        "--momemtum", "0.7",
        "--p-multi-scale", "0.25",
        "--coco"
    ]

    print(f"Executing: {' '.join(cmd)}")

    try:
        result = subprocess.run(
            cmd,
            env=env,
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )

        print(result.stdout)

        if result.returncode != 0:
            print(f"Error running MPAD generation for {stage}:")
            print(result.stderr)
            return False

    except Exception as e:
        print(f"Exception occurred: {e}")
        return False

    # Post-process 실행
    print(f"\nRunning post-processing for {stage}...")
    post_cmd = [
        "python", "mpad_generation/post_process.py",
        dataset_path,
        str(sid),
        str(num_aug_per_image)
    ]

    print(f"Executing: {' '.join(post_cmd)}")

    try:
        post_result = subprocess.run(
            post_cmd,
            env=env,
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )

        print(post_result.stdout)

        if post_result.returncode != 0:
            print(f"Error in post-processing for {stage}:")
            print(post_result.stderr)
            return False

    except Exception as e:
        print(f"Exception in post-processing: {e}")
        return False

    print(f"MPAD generation and post-processing completed for {stage}")
    return True


def organize_generated_data(dataset_path, stage, novel_classes, selected_images):
    """
    생성된 데이터를 정리하고 ImageSets/Main_fewshot에 결과 저장

    Args:
        dataset_path: 데이터셋 경로
        stage: stage 이름 (t2, t3, t4)
        novel_classes: novel class 리스트
        selected_images: {class_name: [image_ids]} 형태의 선택된 이미지
    """
    print(f"\n{'=' * 60}")
    print(f"Organizing Generated Data for {stage.upper()}")
    print(f"{'=' * 60}\n")

    # 출력 디렉토리 생성
    output_dirs = {
        'jpeg': os.path.join(dataset_path, "JPEGImages_gen", stage),
        'anno': os.path.join(dataset_path, "Annotations_gen", stage),
    }

    for dir_path in output_dirs.values():
        os.makedirs(dir_path, exist_ok=True)

    # 생성된 데이터 소스 경로
    src_jpeg_dir = os.path.join(dataset_path, "JPEGImages_gen")
    src_anno_dir = os.path.join(dataset_path, "Annotations_gen")

    # 원본 이미지도 포함
    original_jpeg_dir = os.path.join(dataset_path, "JPEGImages")
    original_anno_dir = os.path.join(dataset_path, "Annotations")

    # 선택된 이미지 파일명 수집
    selected_fileids = []
    for cls, imgs in selected_images.items():
        selected_fileids.extend(imgs)
    selected_fileids = list(set(selected_fileids))  # 중복 제거

    # 복사할 파일 리스트
    copied_files = []

    # 원본 이미지 복사 (선택된 이미지만)
    for fileid in selected_fileids:
        src_jpg = os.path.join(original_jpeg_dir, f"{fileid}.jpg")
        src_xml = os.path.join(original_anno_dir, f"{fileid}.xml")

        if not os.path.exists(src_jpg) or not os.path.exists(src_xml):
            continue

        dst_jpg = os.path.join(output_dirs['jpeg'], f"{fileid}.jpg")
        dst_xml = os.path.join(output_dirs['anno'], f"{fileid}.xml")

        shutil.copy2(src_jpg, dst_jpg)
        shutil.copy2(src_xml, dst_xml)
        copied_files.append(fileid)

    # 증강된 이미지 복사
    if os.path.exists(src_jpeg_dir):
        for filename in os.listdir(src_jpeg_dir):
            if filename.endswith('.jpg'):
                src_file = os.path.join(src_jpeg_dir, filename)
                dst_file = os.path.join(output_dirs['jpeg'], filename)

                if os.path.isfile(src_file):
                    shutil.copy2(src_file, dst_file)

                    # XML도 복사
                    xml_filename = filename.replace('.jpg', '.xml')
                    src_xml = os.path.join(src_anno_dir, xml_filename)
                    dst_xml = os.path.join(output_dirs['anno'], xml_filename)

                    if os.path.exists(src_xml):
                        shutil.copy2(src_xml, dst_xml)
                        copied_files.append(filename.replace('.jpg', ''))

    # ImageSets/Main_fewshot에 결과 저장
    fewshot_dir = os.path.join(dataset_path, "ImageSets", "Main_fewshot")
    os.makedirs(fewshot_dir, exist_ok=True)

    imageset_file = os.path.join(fewshot_dir, f"{stage}_augmented.txt")
    with open(imageset_file, 'w') as f:
        for fileid in sorted(copied_files):
            f.write(f"{fileid}\n")

    print(f"Total {len(copied_files)} files copied to {stage} directories")
    print(f"ImageSet file created: {imageset_file}")
    print(f"  - Original images: {len(selected_fileids)}")
    print(f"  - Augmented images: {len(copied_files) - len(selected_fileids)}")

    return copied_files


def create_ft_stages(dataset_path, stages_to_process):
    """
    Fine-tuning stage 파일 생성 (누적)
    ImageSets/Main_fewshot에서 읽어서 생성
    - t2_ft = t1 + t2
    - t3_ft = t1 + t2 + t3
    - t4_ft = t1 + t2 + t3 + t4

    Args:
        dataset_path: 데이터셋 경로
        stages_to_process: 처리할 stage 리스트
    """
    print(f"\n{'=' * 60}")
    print(f"Creating Fine-Tuning Stage Files")
    print(f"{'=' * 60}\n")

    fewshot_dir = os.path.join(dataset_path, "ImageSets", "Main_fewshot")
    os.makedirs(fewshot_dir, exist_ok=True)

    for ft_stage, component_stages in FT_STAGE_CONFIG.items():
        # 필요한 stage들이 모두 처리되었는지 확인
        all_needed = all(s in stages_to_process for s in component_stages)

        if not all_needed:
            print(f"Skipping {ft_stage} (not all component stages processed)")
            continue

        print(f"\nCreating {ft_stage} from: {', '.join(component_stages)}")

        # 각 component stage의 파일들을 모음
        all_fileids = set()

        for stage in component_stages:
            # Main_fewshot에서 읽기
            if stage == 't1':
                stage_file = os.path.join(fewshot_dir, "t1_sampled.txt")
            else:
                stage_file = os.path.join(fewshot_dir, f"{stage}_augmented.txt")

            if not os.path.exists(stage_file):
                print(f"  Warning: {stage_file} not found, skipping {stage}")
                continue

            with open(stage_file, 'r') as f:
                fileids = [line.strip() for line in f.readlines()]
                all_fileids.update(fileids)
                print(f"  - {stage}: {len(fileids)} images")

        # ft stage 파일 Main_fewshot에 저장
        ft_file = os.path.join(fewshot_dir, f"{ft_stage}.txt")
        with open(ft_file, 'w') as f:
            for fileid in sorted(all_fileids):
                f.write(f"{fileid}\n")

        print(f"  Total: {len(all_fileids)} images")
        print(f"  Saved to: {ft_file}")

    print(f"\n{'=' * 60}")
    print(f"Fine-Tuning Stage Files Created")
    print(f"{'=' * 60}")


def create_final_mapping(dataset_path, stages=['t1', 't2', 't3', 't4']):
    """
    최종 매핑 JSON 생성

    Format: {"파일명": {"shot_idx": 이미지번호, "class_idx": COCO 80개 중 idx}}

    Args:
        dataset_path: 데이터셋 경로
        stages: stage 리스트
    """
    print(f"\n{'=' * 60}")
    print(f"Creating Final Mapping JSON")
    print(f"{'=' * 60}\n")

    final_mapping = {}

    for stage in stages:
        # t1은 원본 Annotations에서, 나머지는 Annotations_gen에서 읽기
        if stage == 't1':
            anno_dir = os.path.join(dataset_path, "Annotations")
            # t1.txt에서 파일 목록 읽기
            tasks_dir = os.path.join(dataset_path, "tasks", "M-OWODB")
            t1_file = os.path.join(tasks_dir, "t1.txt")

            if not os.path.exists(t1_file):
                print(f"Warning: {t1_file} does not exist, skipping t1...")
                continue

            with open(t1_file, 'r') as f:
                t1_fileids = [line.strip() for line in f.readlines()]

            # t1의 novel classes는 VOC_CLASS_NAMES
            novel_classes = VOC_CLASS_NAMES

            # t1 파일들 처리
            class_shot_counters = defaultdict(int)

            for fileid in t1_fileids:
                # VOC2007, VOC2012 둘 다 확인
                xml_file = None
                for voc_dir in ["VOC2007", "VOC2012"]:
                    temp_xml = os.path.join(dataset_path, voc_dir, "Annotations", f"{fileid}.xml")
                    if os.path.exists(temp_xml):
                        xml_file = temp_xml
                        break

                if not xml_file:
                    continue

                tree = ET.parse(xml_file)

                # 이미지에 포함된 novel class들
                novel_classes_in_image = set()
                for obj in tree.findall("object"):
                    cls_name = obj.find("name").text
                    if cls_name in novel_classes:
                        novel_classes_in_image.add(cls_name)

                # 대표 클래스 선택 (첫 번째 novel class)
                if novel_classes_in_image:
                    primary_class = sorted(novel_classes_in_image)[0]
                    class_idx = ALL_COCO_CLASSES.index(primary_class)

                    # shot_idx 할당
                    shot_idx = class_shot_counters[primary_class]
                    class_shot_counters[primary_class] += 1

                    final_mapping[fileid] = {
                        "shot_idx": shot_idx,
                        "class_idx": class_idx
                    }

            print(f"Processed t1: {len([k for k in final_mapping.keys() if k in t1_fileids])} files")
            continue

        # t2, t3, t4 처리 (기존 코드)
        anno_dir = os.path.join(dataset_path, "Annotations_gen", stage)

        if not os.path.exists(anno_dir):
            print(f"Warning: {anno_dir} does not exist, skipping...")
            continue

        # 해당 stage의 novel classes
        novel_classes = STAGE_CONFIG[stage]['novel_classes']

        # shot_idx 카운터 (각 클래스별)
        class_shot_counters = defaultdict(int)

        # XML 파일들을 읽어서 매핑 생성
        for xml_file in sorted(os.listdir(anno_dir)):
            if not xml_file.endswith('.xml'):
                continue

            fileid = xml_file.replace('.xml', '')
            xml_path = os.path.join(anno_dir, xml_file)

            tree = ET.parse(xml_path)

            # 이미지에 포함된 novel class들
            novel_classes_in_image = set()
            for obj in tree.findall("object"):
                cls_name = obj.find("name").text
                if cls_name in novel_classes:
                    novel_classes_in_image.add(cls_name)

            # 대표 클래스 선택 (첫 번째 novel class)
            if novel_classes_in_image:
                primary_class = sorted(novel_classes_in_image)[0]
                class_idx = ALL_COCO_CLASSES.index(primary_class)

                # shot_idx 할당
                shot_idx = class_shot_counters[primary_class]
                class_shot_counters[primary_class] += 1

                final_mapping[fileid] = {
                    "shot_idx": shot_idx,
                    "class_idx": class_idx
                }

    # JSON 파일로 저장
    output_file = os.path.join(dataset_path, "final_mapping.json")
    with open(output_file, 'w') as f:
        json.dump(final_mapping, f, indent=2)

    print(f"Final mapping saved to: {output_file}")
    print(f"Total mapped files: {len(final_mapping)}")

    return final_mapping


def main():
    """메인 함수"""

    # 설정
    dataset_path = "datasets/coco"  # 실제 경로
    num_images_per_class_t1 = 15  # t1: 각 클래스당 15개
    num_images_per_class = 5  # t2,t3,t4: 각 클래스당 5개
    num_aug_per_image = 10
    stages_to_process = ['t1', 't2', 't3', 't4']  # t1 추가

    print("=" * 60)
    print("MPAD Multi-Stage Augmentation Pipeline")
    print("=" * 60)
    print(f"Dataset Path: {dataset_path}")
    print(f"T1 images per class: {num_images_per_class_t1}")
    print(f"T2/T3/T4 images per class: {num_images_per_class}")
    print(f"Augmentations per image: {num_aug_per_image}")
    print(f"Stages: {stages_to_process}")
    print("=" * 60)

    # 0. t1 샘플링 (t1이 stages_to_process에 포함된 경우)
    if 't1' in stages_to_process:
        print(f"\n\n{'#' * 60}")
        print(f"# Sampling T1 from ImageSets/Main/t1.txt")
        print(f"{'#' * 60}\n")

        create_t1_sampled(dataset_path, num_images_per_class_t1)

    # 각 stage별로 처리 (t2, t3, t4만 MPAD 증강)
    for stage in stages_to_process:
        if stage == 't1':
            # t1은 위에서 이미 처리했으므로 스킵
            continue

        config = STAGE_CONFIG[stage]

        print(f"\n\n{'#' * 60}")
        print(f"# Processing {stage.upper()}")
        print(f"# Base Classes: {len(config['base_classes'])}")
        print(f"# Novel Classes: {len(config['novel_classes'])}")
        print(f"{'#' * 60}\n")

        # 1. 이미지 선택
        print(f"[Step 1/4] Selecting images for {stage}")
        selected_images = select_images_per_class(
            dataset_path,
            stage,
            config['novel_classes'],
            num_images_per_class
        )

        total_selected = sum(len(imgs) for imgs in selected_images.values())
        print(f"Selected {total_selected} images across {len(selected_images)} classes")

        for cls, imgs in selected_images.items():
            print(f"  - {cls}: {len(imgs)} images")

        # 2. MPAD 증강 실행
        print(f"\n[Step 2/4] Running MPAD generation for {stage}")
        success = run_mpad_generation(
            dataset_path,
            stage,
            config['sid'],
            selected_images,  # 선택된 이미지 정보 전달
            num_aug_per_image
        )

        if not success:
            print(f"Failed to generate data for {stage}, skipping...")
            continue

        # 3. 생성된 데이터 정리
        print(f"\n[Step 3/4] Organizing generated data for {stage}")
        copied_files = organize_generated_data(
            dataset_path,
            stage,
            config['novel_classes'],
            selected_images  # selected_images 전달
        )

        print(f"\nStage {stage} completed successfully!")
        print(f"Total files: {len(copied_files)}")

    # 4. Fine-tuning stage 파일 생성
    print(f"\n[Step 4/5] Creating fine-tuning stage files")
    create_ft_stages(dataset_path, stages_to_process)

    # 5. 최종 매핑 생성
    print(f"\n[Step 5/5] Creating final mapping JSON")
    final_mapping = create_final_mapping(dataset_path, stages_to_process)

    print("\n" + "=" * 60)
    print("ALL STAGES COMPLETED SUCCESSFULLY!")
    print("=" * 60)

    # 결과 요약
    print("\nGenerated Directory Structure:")
    print("\nBase Stage:")
    print("  - ImageSets/Main_fewshot/t1_sampled.txt")

    for stage in stages_to_process:
        if stage == 't1':
            continue
        print(f"\n{stage.upper()}:")
        print(f"  - JPEGImages_gen/{stage}/")
        print(f"  - Annotations_gen/{stage}/")
        print(f"  - ImageSets/Main_fewshot/{stage}_augmented.txt")

    print("\nFine-tuning Stages:")
    for ft_stage in FT_STAGE_CONFIG.keys():
        print(f"  - ImageSets/Main_fewshot/{ft_stage}.txt")

    print(f"\nFinal mapping: {dataset_path}/final_mapping.json")
    print(f"Total mapped entries: {len(final_mapping)}")


if __name__ == "__main__":
    main()

    for stage in stages_to_process:
        if stage == 't1':
            continue
        print(f"\n{stage.upper()}:")
        print(f"  - JPEGImages_gen/{stage}/")
        print(f"  - Annotations_gen/{stage}/")
        print(f"  - ImageSets_gen/{stage}/{stage}_augmented.txt")

    print("\nFine-tuning Stages:")
    for ft_stage in FT_STAGE_CONFIG.keys():
        print(f"  - tasks/M-OWODB/{ft_stage}.txt")

    print(f"\nFinal mapping: {dataset_path}/final_mapping.json")
    print(f"Total mapped entries: {len(final_mapping)}")

if __name__ == "__main__":
    main()






