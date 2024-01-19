import os
import subprocess
from glob import glob

input_glob = '/home/tim/Downloads/maries_filer/**/*.mov'

output_dir = '/home/tim/Work/nexa/nexa-audio-normalization/data/normalized_audio_video'

# Ensure directories exist
os.makedirs(output_dir, exist_ok=True)


# List all MOV files in the input folder
paths = glob(input_glob, recursive=True)


command = 'ffmpeg-normalize -f "{}" -of {} -c:a aac -b:a 320k'.format('" "'.join(paths[:10]), output_dir)

print(command)

subprocess.call(command, shell=True)
