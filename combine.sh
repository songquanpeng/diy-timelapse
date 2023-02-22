#!/bin/bash
python process.py --input $1 --output $1_processed
ffmpeg -r 30 -i $1_processed/%04d.jpg -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p $1.mp4