#!/bin/bash
#
# MPAD Multi-Stage Augmentation Runner
# t2, t3, t4를 각각 novel class로 설정하여 MPAD 증강 실행
#

set -e  # 에러 발생시 중단

# ===== 설정 =====
DATASET_PATH="datasets/coco"
NUM_IMAGES_PER_CLASS_T1=15  # t1: 각 클래스당 15개
NUM_IMAGES_PER_CLASS=5      # t2,t3,t4: 각 클래스당 5개
NUM_AUG_PER_IMAGE=10
STAGES="t1 t2 t3 t4"  # 공백으로 구분

# CUDA 디바이스 설정
export CUDA_VISIBLE_DEVICES=0

# ===== 색상 정의 =====
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# ===== 함수 정의 =====
print_header() {
    echo -e "${BLUE}============================================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}============================================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# ===== 메인 스크립트 =====
print_header "MPAD Multi-Stage Augmentation Pipeline"

echo "Dataset Path: $DATASET_PATH"
echo "Images per class: $NUM_IMAGES_PER_CLASS"
echo "Augmentations per image: $NUM_AUG_PER_IMAGE"
echo "Stages to process: $STAGES"
echo ""

# 데이터셋 경로 확인
if [ ! -d "$DATASET_PATH" ]; then
    print_error "Dataset path not found: $DATASET_PATH"
    exit 1
fi

# 필요한 디렉토리 확인
REQUIRED_DIRS=(
    "$DATASET_PATH/JPEGImages"
    "$DATASET_PATH/Annotations"
    "$DATASET_PATH/ImagesSets/Main"
)

for dir in "${REQUIRED_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        print_error "Required directory not found: $dir"
        exit 1
    fi
done

print_success "All required directories found"

# PowerPaint weights 확인
if [ ! -d "mpad_generation/PowerPaint/models" ]; then
    print_warning "PowerPaint models directory not found"
    print_warning "Make sure you have downloaded the required weights"
fi

# Python 스크립트 실행
print_header "Running Python augmentation script"
python generate_mpad_for_all_stages.py

# 결과 확인
if [ $? -eq 0 ]; then
    print_success "Augmentation pipeline completed successfully!"

    echo ""
    print_header "Generated Files"

    # t1 확인
    if [ -f "$DATASET_PATH/ImageSets/Main/t1.txt" ]; then
        echo ""
        echo -e "${GREEN}Stage t1:${NC}"
        NUM_T1=$(wc -l < "$DATASET_PATH/ImageSets/Main/t1.txt")
        echo "  - t1.txt: $NUM_T1 images"
    fi

    # t2, t3, t4 확인
    for stage in t2 t3 t4; do
        echo ""
        echo -e "${GREEN}Stage $stage:${NC}"

        if [ -d "$DATASET_PATH/JPEGImages_gen/$stage" ]; then
            NUM_IMAGES=$(ls -1 "$DATASET_PATH/JPEGImages_gen/$stage" | wc -l)
            echo "  - Images: $NUM_IMAGES files"
        fi

        if [ -d "$DATASET_PATH/Annotations_gen/$stage" ]; then
            NUM_ANNOS=$(ls -1 "$DATASET_PATH/Annotations_gen/$stage" | wc -l)
            echo "  - Annotations: $NUM_ANNOS files"
        fi

        if [ -f "$DATASET_PATH/ImageSets_gen/$stage/${stage}_augmented.txt" ]; then
            NUM_IDS=$(wc -l < "$DATASET_PATH/ImageSets_gen/$stage/${stage}_augmented.txt")
            echo "  - ImageSet entries: $NUM_IDS"
        fi
    done

    # Fine-tuning stages 확인
    echo ""
    echo -e "${GREEN}Fine-tuning Stages:${NC}"
    for ft_stage in t2_ft t3_ft t4_ft; do
        if [ -f "$DATASET_PATH/tasks/M-OWODB/${ft_stage}.txt" ]; then
            NUM_FT=$(wc -l < "$DATASET_PATH/tasks/M-OWODB/${ft_stage}.txt")
            echo "  - ${ft_stage}.txt: $NUM_FT images"
        fi
    done

    if [ -f "$DATASET_PATH/final_mapping.json" ]; then
        echo ""
        echo -e "${GREEN}Final Mapping:${NC}"
        echo "  - File: $DATASET_PATH/final_mapping.json"
        NUM_ENTRIES=$(grep -c "shot_idx" "$DATASET_PATH/final_mapping.json" || echo "0")
        echo "  - Entries: $NUM_ENTRIES"
    fi

else
    print_error "Augmentation pipeline failed!"
    exit 1
fi

echo ""
print_header "Pipeline Complete!"
print_success "All stages processed successfully"
echo ""
echo "Next steps:"
echo "  1. Check t1.txt in tasks/M-OWODB/"
echo "  2. Check the generated files in JPEGImages_gen/, Annotations_gen/, ImageSets_gen/"
echo "  3. Review fine-tuning stage files (t2_ft.txt, t3_ft.txt, t4_ft.txt)"
echo "  4. Review the final_mapping.json file"
echo "  5. Use the augmented data for training"
echo ""