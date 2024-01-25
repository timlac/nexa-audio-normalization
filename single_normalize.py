from glob import glob
import subprocess
import os

input_path = "data/box_downloads/A207_pri_p_2.mov"
output_folder = "data/normalized_examples"

# input_glob = "data/examples/**/*.mov"
# output_folder = "data/normalized_examples"

paths = glob(input_path, recursive=True)

normalize_audio = ('ffmpeg-normalize -f -v -ext "mp4" "{}" -of {} '
                   '-c:a aac -b:a 320k -nt peak '
                   '-c:v libx264 -e"-vf scale=1280:720"'
                   .format('" "'.join(paths), output_folder))

print(normalize_audio)

# normalize_audio = ('ffmpeg-normalize -f -v -ext "mp4" "{}" -of {} --dynamic '
#                    '-c:a aac -b:a 320k '
#                    .format('" "'.join(paths), output_folder))

print(normalize_audio)
subprocess.call(normalize_audio, shell=True)
