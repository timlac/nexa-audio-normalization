import os
import subprocess
from glob import glob

input_glob = '/home/tim/Downloads/maries_filer/**/*.mov'

mkv_dir = '/home/tim/Work/nexa/nexa-audio-normalization/out/audio_video_mkv'
merged_mkv_dir = '/home/tim/Work/nexa/nexa-audio-normalization/out/normalized_audio_video_mkv'
raw_audio_dir = '/home/tim/Work/nexa/nexa-audio-normalization/out/raw_audio'
normalized_audio_dir = '/home/tim/Work/nexa/nexa-audio-normalization/out/normalized_audio'
merged_mp4_dir = '/home/tim/Work/nexa/nexa-audio-normalization/out/normalized_audio_video_mp4'

# Ensure directories exist
os.makedirs(mkv_dir, exist_ok=True)
os.makedirs(raw_audio_dir, exist_ok=True)
os.makedirs(normalized_audio_dir, exist_ok=True)
os.makedirs(merged_mkv_dir, exist_ok=True)

ffmpeg_executable = '/usr/bin/ffmpeg'

# List all MOV files in the input folder
paths = glob(input_glob, recursive=True)

# Process each file in the directory
for idx, filepath in enumerate(paths):
    filename = os.path.basename(filepath)
    filename_without_ext = os.path.splitext(filename)[0]

    if filename.endswith('.mov'):
        # Construct file paths
        converted_mkv_path = os.path.join(mkv_dir, filename_without_ext + '.mkv')
        raw_audio_path = os.path.join(raw_audio_dir, filename_without_ext + '.wav')
        normalized_audio_path = os.path.join(normalized_audio_dir, filename_without_ext + '.wav')
        merged_mkv_path = os.path.join(merged_mkv_dir, filename_without_ext + '.mkv')
        merged_mp4_path = os.path.join(merged_mp4_dir, filename_without_ext + ".mp4")

        command = (f'ffmpeg -i "{filepath}" '
                   f'-map 0:v -map 0:a '
                   f'-c:v libx264 -crf 18 -preset slow '
                   f'-c:a aac -b:a 320k "{converted_mkv_path}"')
        print(command)
        # Step 1: Convert MOV to MKV with AAC audio
        subprocess.run(command, shell=True)

        # Step 2: Extract Audio
        command = f'ffmpeg -i "{converted_mkv_path}" -q:a 0 -map a "{raw_audio_path}"'
        print(command)
        subprocess.run(command, shell=True)

        # Normalize Audio
        command = f'ffmpeg -i "{raw_audio_path}" -filter:a loudnorm=I=-23:TP=-1.5:LRA=11 "{normalized_audio_path}"'
        print(command)
        subprocess.run(command, shell=True)

        # Step 3: Merge Normalized Audio back with MKV Video
        command = (f'ffmpeg -i "{converted_mkv_path}" -i "{normalized_audio_path}" '
                   f'-c:v libx264 -crf 18 -preset slow -c:a aac -b:a 320k -map 0:v:0 -map 1:a:0 -shortest "{merged_mkv_path}"')
        print(command)
        subprocess.run(command, shell=True)

        # Convert to MP4
        command = f'ffmpeg -i "{merged_mkv_path}" -c:v copy -c:a copy "{merged_mp4_path}"'
        print(command)
        subprocess.run(command, shell=True)

        # Optional: Remove temporary audio files
        os.remove(converted_mkv_path)
        os.remove(raw_audio_path)
        os.remove(normalized_audio_path)
        os.remove(merged_mkv_path)

        break


print('Normalization process completed.')



# TODO: ERROR is due to there being a space in the path, should be easy to fix...
# /home/tim/Downloads/maries_filer/A402/audio-video: No such file or directory