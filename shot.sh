#!/bin/bash
DAY=$(date +"%Y-%m-%d")
DIR="/home/ubuntu/Pictures/timelapse/$DAY"
mkdir -p $DIR
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
fswebcam --no-banner -r 1920x1080 -S 60 -D 2 -F 2 $DIR/$DATE.jpg