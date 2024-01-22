import os
import subprocess
from glob import glob
from pathlib import Path
from nexa_coding_interpreter.metadata import Metadata
from nexa_py_sentimotion_mapper.sentimotion_mapper import Mapper

fmri_emotions = [
    "anger",
    "anxiety",
    "disgust",
    "sadness",
    "happiness_joy",
    "interest_curiosity",
    "positive_surprise",
    "relief",
    "neutral"
]

fmri_emotion_ids = Mapper.get_emotion_id_from_emotion(fmri_emotions)

print(fmri_emotion_ids)

input_glob = '/home/tim/Downloads/maries_filer/**/*.mov'
output_dir = '/home/tim/Work/nexa/nexa-audio-normalization/data/normalized_audio_video'

# Ensure directories exist
os.makedirs(output_dir, exist_ok=True)
# List all MOV files in the input folder
paths = glob(input_glob, recursive=True)

fmri_paths = []

for path in paths:
    filename = Path(path).stem
    meta = Metadata(filename)
    if meta.mix == 0:
        if meta.emotion_1_id in fmri_emotion_ids:
            fmri_paths.append(path)


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
