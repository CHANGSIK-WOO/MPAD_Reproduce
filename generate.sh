export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
# GENERATIVE_DATA_PATH=datasets/COCOGen_novel
# python mpad_generation/main_generate_data.py --gendata-folder ${GENERATIVE_DATA_PATH} \
#     --bg-clutter \
#     --bg-sim \
#     --fg-rand \
#     --fg-fg --num-fine-grained 4 \
#     --fg-sim --p-fg-sim 0.8 --mix-up 0.7 --momemtum 0.7 \
#     --p-multi-scale 0.25 \
#     --coco \
#     --num-ins 300

sid=2
GENERATIVE_DATA_PATH=datasets/VOCGen_novel${sid}_3
# rm -rf ${GENERATIVE_DATA_PATH}

# python mpad_generation/main_generate_data.py --gendata-folder ${GENERATIVE_DATA_PATH} \
#     --bg-clutter \
#     --bg-rand \
#     --bg-sim \
#     --fg-rand \
#     --fg-fg --num-fine-grained 4 \
#     --fg-sim --p-fg-sim 0.8 --mix-up 0.7 --momemtum 0.8 \
#     --p-multi-scale 0.25 \
#     --sid ${sid} \
#     --num-ins 300

python mpad_generation/post_process.py ${GENERATIVE_DATA_PATH} ${sid} 300
