import os
import subprocess
from glob import glob
from pathlib import Path
from nexa_coding_interpreter.metadata import Metadata
from nexa_py_sentimotion_mapper.sentimotion_mapper import Mapper


input_glob = '/home/tim/Downloads/maries_filer/**/*.mov'
output_dir = '/home/tim/Work/nexa/nexa-audio-normalization/data/normalized_audio_video'

# Ensure directories exist
os.makedirs(output_dir, exist_ok=True)
# List all MOV files in the input folder
paths = glob(input_glob, recursive=True)

fmri_paths = []

for path in paths:
    filename = os.path.basename(path)


command = 'ffmpeg-normalize -f -v -ext "mp4" "{}" -of {} -c:a aac -b:a 320k'.format('" "'.join(fmri_paths), output_dir)
print(command)
subprocess.call(command, shell=True)


# print(len(paths))
#
# batch_size = 500
#
# for i in range(0, len(paths), batch_size):
#     batch = paths[i:i + batch_size]
#     command = 'ffmpeg-normalize -f -v -ext "mp4" "{}" -of {} -c:a aac -b:a 320k'.format('" "'.join(batch), output_dir)
#     print(command)
#     subprocess.call(command, shell=True)
