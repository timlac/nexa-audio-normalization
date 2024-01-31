from glob import glob
import subprocess
import os

from fmri_filter import filter_paths

input_glob = "data/A65_download/**/*.mov"
output_folder = "data/peak_normalized_box_downloads"

# input_glob = "data/examples/**/*.mov"
# output_folder = "data/normalized_examples"


# input_glob = "/home/tim/Downloads/maries_filer/**/*.mov"
# output_folder = "data/peak_normalized_marie"

paths = glob(input_glob, recursive=True)

paths = filter_paths(paths)


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
