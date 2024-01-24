import os
import librosa
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

def detect_silence(audio_file, threshold=0.01, frame_length=2048, hop_length=512):
    # Load the audio file
    y, sr = librosa.load(audio_file)

    # Calculate the RMS energy of the audio using a moving window
    rms = librosa.feature.rms(y=y, frame_length=frame_length, hop_length=hop_length)[0]

    print(f'{rms.max()=}')

    # Threshold for considering a segment as silent
    is_silent = rms < threshold

    return is_silent, rms.max()


def find_silent_files(folder_path, threshold=0.01):
    silent_files = []
    peaks = []

    for filename in os.listdir(folder_path):
        if filename.endswith(('.mov', '.mp4', '.mkv')):  # Add more audio file formats if needed
            audio_file = os.path.join(folder_path, filename)

            print(f"detecting {filename}")
            is_silent, peak = detect_silence(audio_file, threshold=threshold)

            peaks.append(peak)

            if all(is_silent):
                silent_files.append(audio_file)

    return silent_files, peaks


folder_path = '../data/peak_normalized_box_downloads'
silent_threshold = 0.001  # Adjust this threshold as needed

silent_files, peaks = find_silent_files(folder_path, threshold=silent_threshold)

if silent_files:
    print("Silent files found:")
    for file in silent_files:
        print(file)
else:
    print("No silent files found.")


plt.hist(peaks, bins=100, edgecolor='black')  # Adjust the number of bins as needed
plt.xlabel('Peaks')
plt.ylabel('Frequency')
plt.title('Histogram of peak levels')
plt.grid(True)
plt.show()
