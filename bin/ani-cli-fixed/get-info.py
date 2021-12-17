#!/usr/bin/env python3
import os
import subprocess

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

movies = []

for file in os.listdir("."):
    if file.endswith(".mkv") or file.endswith(".mp4"):
        duration = get_length(file)
        movies.append((file, duration))


while movies:
    maxdur = -1
    maxi = 0
    for i in range(len(movies)):
        if movies[i][1] > maxdur:
            maxdur = movies[i][1]
            maxi = i

    curlen = int(round(movies[maxi][1], 0))
    hours = curlen//3600
    curlen-=hours*3600
    minutes=curlen//60
    curlen-=minutes*60
    seconds=curlen

    print(f"{movies[maxi][0]} \t->\t {hours}h{minutes}m{seconds}s")
    movies.pop(maxi)
