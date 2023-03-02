#!/bin/bash
python process.py --input $1 --output $1_processed
python adjust_saturation.py --input $1_processed --output $1_processed --saturation_factor 1.8
ffmpeg -r 10 -i $1_processed/%04d.jpg -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p $1.mp4 -y