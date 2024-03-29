## Normalization

Tried different normalization techniques using [ffmpeg](https://ffmpeg.org/), difficult to find a normalization method that manages to normalize all clips equivalently, 
some clips, e.g. `A402_pea_v_1.mov` have very low volume and the volume remains low post normalization.

Encountered weird error when working with `.mov` or `.mp4` files:

> [mp4 @ 0x5563df05d540] Application provided duration: -9223372036854775808
/ timestamp: -9223372036854775808 is out of range for mov/mp4 format
[mp4 @ 0x5563df05d540] pts has no value

Spent some time investigating this trying out various methods, the only method that did not reproduce the bug was when I instead worked with `.mkv` files.

Then I instead moved to working with a wrapper library for ffmpeg called [ffmpeg-normalize](https://github.com/slhck/ffmpeg-normalize), 
which handles clips with very low volume more efficiently, and handles the audio separation and re-merging automatically. 

When running ffmpeg some of the normalized videos are silenced. However, converting the audio to AAC codec when running the normalization seems to fix this error. 


Upon further experimentation it turns out that some videos do not get properly increased loudness using Loudness Normalization. 

### Original files

![histogram_original_files.png](plots%2Fhistogram_original_files.png)

As illustrated in the histogram below there is a clear collection of outliers around 0.0

### Loudness Normalized Files

![histogram loudness normalized files.png](plots%2Fhistogram_loudness_normalized_files.png)

This is however handled better using Peak Normalization instead, which produces no outliers:

### Peak Normalized Files

![histogram_peak_normalized_files.png](plots%2Fhistogram_peak_normalized_files.png)

## Video Collection

Note, currently rely on dev token authentication. Awaiting administrator approval for JWT token. Ticket pending. 


Video id number `A327` does not seem to have the emotion sadness... 

Video id number `A55` has a lot of different versions, maybe remove some? 

Video id number `A65` does not have any un-normalized clips in the folder, skipping... 

Video `A408_neu_sit4_p` has some kind of high pitch sound in the beginning making the effectively making the other sounds lower in normalization:

![waveforms_A408_neu_sit4_p.png](plots%2Fwaveforms_A408_neu_sit4_p.png)

Video `A207_pri_p_2` is completely silent, peak normalization fails. 

Video `A200_neu_sit4_p` has a weird audio pattern and is silent:

![A200_neu_sit4_p.wave.png](plots%2FA200_neu_sit4_p.wave.png)

TODO: REMOVE THIS FILE FROM AUDIO