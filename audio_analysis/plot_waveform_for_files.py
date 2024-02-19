import librosa
import librosa.display
import matplotlib.pyplot as plt
import glob

audio_files = glob.glob("../data/fmri/peak_normalized_fmri_video/**/*.mp4", recursive=True)

print(audio_files[0])

y1, sr1 = librosa.load(audio_files[0])
y2, sr2 = librosa.load(audio_files[1])
y3, sr3 = librosa.load(audio_files[2])


plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
librosa.display.waveshow(y1, sr=sr1)

# plt.subplot(3, 1, 2)
# librosa.display.waveshow(y2, sr=sr2)
#
# plt.subplot(3, 1, 3)
# librosa.display.waveshow(y3, sr=sr3)

plt.tight_layout()
plt.show()
