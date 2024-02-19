import subprocess
import os

# Define the input and output directories
input_dir = 'data/fmri/peak_normalized_fmri'
audio_output_dir = 'data/fmri/peak_normalized_fmri_audio'
video_output_dir = 'data/fmri/peak_normalized_fmri_video'

# Create the output directories if they don't exist
if not os.path.exists(audio_output_dir):
    os.makedirs(audio_output_dir)
if not os.path.exists(video_output_dir):
    os.makedirs(video_output_dir)

# Loop through each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.mp4'):
        input_path = os.path.join(input_dir, filename)

        # Construct output filenames
        audio_output_path = os.path.join(audio_output_dir, filename)
        video_output_path = os.path.join(video_output_dir, filename)

        # Extract audio using FFmpeg
        subprocess.run(['ffmpeg', '-i', input_path, '-vn', '-acodec', 'copy', audio_output_path], check=True)

        # Extract video (no audio) using FFmpeg
        subprocess.run(['ffmpeg', '-i', input_path, '-an', '-vcodec', 'copy', video_output_path], check=True)

print("Extraction completed.")
