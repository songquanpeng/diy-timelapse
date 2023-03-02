#!/bin/bash
python process.py --input $1 --output $1_processed
python adjust.py --input $1_processed --output $1_processed --saturation 2 --temperature 0 --tint 0
ffmpeg -r 10 -i $1_processed/%04d.jpg -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p $1.mp4 -y