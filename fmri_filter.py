from nexa_py_sentimotion_mapper.sentimotion_mapper import Mapper
from nexa_coding_interpreter.metadata import Metadata
from pathlib import Path

fmri_emotions = [
    "anger",
    "anxiety",
    "disgust",
    "sadness",
    "happiness_joy",
    "interest_curiosity",
    "pride",
    "relief",
    "neutral"
]

fmri_emotion_ids = Mapper.get_emotion_id_from_emotion(fmri_emotions)


def belongs_to_fmri_dataset(filename):
    """
    The FMRI dataset should only contain 9 different emotions, and no mixed emotions.
    :param filename:
    :return: True or False
    """
    filename_no_ext = Path(filename).stem

    meta = Metadata(filename_no_ext)
    if meta.mix == 1:
        return False
    if meta.mode == "v":
        return False
    if meta.intensity_level == 1 or meta.intensity_level == 4:
        return False
    if meta.emotion_1_id not in fmri_emotion_ids:
        return False

    return True


def filter_paths(paths):
    ret = []
    for path in paths:
        if belongs_to_fmri_dataset(path):
            ret.append(path)
        else:
            print("skipping path with non-valid metadata: " + str(path))
    return ret
