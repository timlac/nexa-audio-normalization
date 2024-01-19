import os
import subprocess
from glob import glob

input_glob = '/home/tim/Downloads/maries_filer/**/*.mov'

normalized_audio_dir = '/home/tim/Work/nexa/nexa-audio-normalization/out/normalized_audio'
output_dir = '/home/tim/Work/nexa/nexa-audio-normalization/out/normalized_audio_video'

# Ensure directories exist
os.makedirs(normalized_audio_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

ffmpeg_executable = '/usr/bin/ffmpeg'

# List all MOV files in the input folder
paths = glob(input_glob, recursive=True)

# Process each file in the directory
for idx, filepath in enumerate(paths):
    filename = os.path.basename(filepath)
    filename_without_ext = os.path.splitext(filename)[0]

    if filename.endswith('.mov'):
        # Construct file paths
        raw_audio_path = os.path.join(normalized_audio_dir, filename_without_ext + '.wav')
        normalized_audio_path = os.path.join(normalized_audio_dir, filename_without_ext + '_normalized.wav')
        output_path = os.path.join(output_dir, filename)

        # Step 1: Extract Audio
        command = f'ffmpeg -i "{filepath}" -q:a 0 -map a "{raw_audio_path}"'
        print(command)
        subprocess.run(command, shell=True)

        # Step 2: Normalize Audio
        command = f'ffmpeg -i "{raw_audio_path}" -filter:a loudnorm=I=-23:TP=-1.5:LRA=11 "{normalized_audio_path}"'
        print(command)
        subprocess.run(command, shell=True)

        # Step 3: Merge Normalized Audio back with Original Video
        command = (f'ffmpeg -i "{filepath}" -i "{normalized_audio_path}" '
                   f'-c:v copy -c:a copy -map 0:v:0 -map 1:a:0 -shortest "{output_path}"')
        print(command)
        subprocess.run(command, shell=True)

        # Optional: Remove temporary audio files
        # os.remove(raw_audio_path)
        # os.remove(normalized_audio_path)

        if idx >= 10:  # Process only the first 10 files for testing
            break

print('Normalization process completed.')