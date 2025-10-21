#!/usr/bin/env bash

#SBATCH --job-name=MPAD_GEN_ALL
#SBATCH --nodes=1
#SBATCH --gres=gpu:2
#SBATCH -p batch
#SBATCH -w vgi1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem=30G
#SBATCH --time=2-0
#SBATCH -o ./logs/%N_%x_%j.out
#SBATCH -e ./logs/%N_%x_%j.err

set -euo pipefail
source "$HOME/anaconda3/etc/profile.d/conda.sh"
conda activate PowerPaint

# 로그 디렉토리 생성
mkdir -p logs

# 설정
GENERATIVE_DATA_PATH=datasets/coco/
NUM_INS=4

# GPU 개수 확인
GPUS=$(python -c "import torch; print(torch.cuda.device_count())")
echo "Number of GPUs: ${GPUS}"

# t1, t2, t3, t4 순차 실행
for sid in "t1" "t2" "t3" "t4"
do
    echo "====================================="
    echo "Starting sid=${sid}"
    echo "====================================="

    # 데이터 생성
    torchrun \
      --nproc_per_node=${GPUS} \
      --standalone \
      mpad_generation/main_generate_data.py \
      --gendata-folder ${GENERATIVE_DATA_PATH} \
      --bg-rand \
      --bg-clutter \
      --bg-sim \
      --fg-rand \220409

      --fg-fg --num-fine-grained 4 \
      --fg-sim --p-fg-sim 0.8 --mix-up 0.7 --momemtum 0.7 \
      --p-multi-scale 0.25 \
      --num-ins ${NUM_INS} \
      --sid ${sid} \
      --coco

    # 후처리
    python mpad_generation/post_process.py ${GENERATIVE_DATA_PATH} ${sid} ${NUM_INS}

    echo "====================================="
    echo "Completed sid=${sid}"
    echo "====================================="
    echo ""
done

echo "All tasks completed!"
