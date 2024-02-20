import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from nexa_coding_interpreter.metadata import Metadata
from pathlib import Path

import warnings
warnings.filterwarnings('ignore')


def detect_rms(audio_file, threshold=0.01, frame_length=2048, hop_length=512):
    # Load the audio file
    y, sr = librosa.load(audio_file)

    # Calculate the RMS energy of the audio using a moving window
    ret_rms = librosa.feature.rms(y=y, frame_length=frame_length, hop_length=hop_length)[0]

    return ret_rms


def rms_to_db(input_rms, ref=1.0, epsilon=1e-10):
    inp = np.maximum(epsilon, input_rms)

    # Convert RMS values to decibels
    return 20 * np.log10(inp/ref)


path = '../data/original_validation_experiment/*.mp4'
glob_audio_files = glob(path)

rms_dict = {}
rms_peak_dict = {}
rms_peak_db_dict = {}


for idx, af in enumerate(glob_audio_files):
    print(f'Processing {af} {idx}/{len(glob_audio_files)}')

    filename = os.path.basename(af)
    rms = detect_rms(af)
    rms_peak = np.max(rms)
    rms_peak_db = rms_to_db(rms_peak)

    rms_dict[filename] = rms
    rms_peak_dict[filename] = rms_peak
    rms_peak_db_dict[filename] = rms_peak_db


# Assuming rms_peak_db_dict contains your peak dB levels for each file
peak_levels_db = list(rms_peak_db_dict.values())

# Calculate the mean and standard deviation
mean_db = np.mean(peak_levels_db)
std_dev_db = np.std(peak_levels_db)

print(f"Mean Peak Level (dB): {mean_db:.2f}")
print(f"Standard Deviation of Peak Levels (dB): {std_dev_db:.2f}")


plt.hist(rms_peak_db_dict.values(), bins=300, edgecolor='black')  # Adjust the number of bins as needed
plt.xlabel('Peaks')
plt.ylabel('Frequency')
plt.title('Histogram of peak levels')
plt.grid(True)
plt.show()

plt.boxplot(rms_peak_db_dict.values())
plt.xlabel('Audio Files')
plt.ylabel('Peak Levels (dB)')
plt.title('Distribution of Peak Levels in Decibels')
plt.grid(True)
plt.show()

sorted_tuples = sorted(rms_peak_db_dict.items(), key=lambda item: item[1])
sorted_dict = dict(sorted_tuples)
print(sorted_dict)


for key, val in sorted_dict.items():
    filename_no_ext = Path(key).stem
    meta = Metadata(filename_no_ext)

    if meta.mode == "p":
        print(f'filename: {filename_no_ext}, rms_peak_db: {val}')
