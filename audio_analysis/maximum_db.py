import librosa
import numpy as np
from glob import glob
import os
import matplotlib.pyplot as plt


def detect_maximum_db(audio_file):
    y, sr = librosa.load(audio_file)

    # Step 2: Convert to STFT
    S = librosa.stft(y)

    # Convert to amplitude
    amp = np.abs(S)

    # Convert amplitude to decibels
    db = librosa.amplitude_to_db(amp, ref=np.max)

    # Step 3: Find the maximum sound level in decibels
    return np.max(db)


# Step 1: Load the audio file
path = '../data/original_validation_experiment/*.mp4'

glob_audio_files = glob(path)

db_dict = {}

i = 0
for af in glob_audio_files:
    filename = os.path.basename(af)
    max_db = detect_maximum_db(af)
    db_dict[filename] = max_db
    i += 1
    if i > 20:
        break

plt.hist(db_dict.values(), bins=100, edgecolor='black')  # Adjust the number of bins as needed
plt.xlabel('Peaks')
plt.ylabel('Frequency')
plt.title('Histogram of peak levels')
plt.grid(True)
plt.show()
