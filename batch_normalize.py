from glob import glob
import subprocess

input_glob = "data/box_downloads/**/*.mov"
output_folder = "data/normalized_box_downloads"


paths = glob(input_glob, recursive=True)

print(paths)

command = ('ffmpeg-normalize -f -v -ext "mp4" "{}" -of {} -c:a aac -b:a 320k'
           .format('" "'.join(paths), output_folder))

print(command)
subprocess.call(command, shell=True)