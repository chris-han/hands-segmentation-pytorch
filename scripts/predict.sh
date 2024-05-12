#!/bin/bash

python main.py \
    --mode predict \
    --data_base_path './data_set/0200A1795784_frames' \
    --model_checkpoint "./checkpoint/checkpoint.ckpt" \
    --model_pretrained
