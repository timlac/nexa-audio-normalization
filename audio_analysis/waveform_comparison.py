import librosa
import librosa.display
import matplotlib.pyplot as plt

filename = "A405_neu_sit1_p"

audio_file1 = f"../data/box_downloads/{filename}.mov"  # Replace with the path to your first audio file
audio_file2 = f"../data/normalized_box_downloads/{filename}.mp4"  # Replace with the path to your second audio file
audio_file3 = f"../data/peak_normalized_box_downloads/{filename}.mp4"  # Replace with the path to your third audio file

y1, sr1 = librosa.load(audio_file1)
y2, sr2 = librosa.load(audio_file2)
y3, sr3 = librosa.load(audio_file3)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
librosa.display.waveshow(y1, sr=sr1)
plt.title("Waveform for Original audio")

plt.subplot(3, 1, 2)
librosa.display.waveshow(y2, sr=sr2)
plt.title("Waveform for Loudness Normalized audio")

plt.subplot(3, 1, 3)
librosa.display.waveshow(y3, sr=sr3)
plt.title("Waveform for Peak Normalized audio")

plt.tight_layout()
plt.show()
