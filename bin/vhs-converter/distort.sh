#!/bin/bash

if [[ $# -ne 2 ]]; then
	echo "Arguments required: INPUT OUTPUT"
	exit 1
fi

ffmpeg -i raw-over.webm -vf scale=720:480 over.mp4
ffmpeg -i $1 -vf scale=720:480 input.mp4

ffmpeg -i input.mp4 -vf convolution="-2 -1 0 -1 1 1 0 1 2:-2 -1 0 -1 1 1 0 1 2:-2 -1 0 -1 1 1 0 1 2:-2 -1 0 -1 1 1 0 1 2" -c:a copy out.mp4

DURATION="$(ffprobe -i out.mp4 -show_entries format=duration -v quiet -of csv='p=0')"
ffmpeg -stream_loop -1 -i out.mp4 -i over.mp4 -filter_complex "[1:v]format=rgba,colorchannelmixer=aa=0.6,loop=-1:1000:0,setpts=N/FRAME_RATE/TB[fg];[0][fg]blend='screen'" -t $DURATION $2

rm input.mp4 out.mp4 over.mp4
