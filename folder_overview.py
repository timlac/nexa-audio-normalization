import os
from pathlib import Path

from nexa_coding_interpreter.metadata import Metadata

overview = {}

for filename in os.listdir("data/box_downloads"):
    filename_no_ext = Path(filename).stem

    meta = Metadata(filename_no_ext)

    if meta.emotion_1_id not in overview.keys():
        overview[meta.emotion_1_id] = []

    overview[meta.emotion_1_id].append(filename)


print(len(overview.keys()))

total_length = 0

for key, val in overview.items():
    print(f"{key}: {len(val)}")

    total_length += len(val)

print(total_length)