from nexa_coding_interpreter.metadata import Metadata
from pathlib import Path


def belongs_to_main_validation_study(filename):
    """
    No mixed emotions, only intensity level
    :param filename:
    :return: True or False
    """
    filename_no_ext = Path(filename).stem

    meta = Metadata(filename_no_ext)
    if meta.mix == 1:
        return False
    if meta.intensity_level == 1 or meta.intensity_level == 4:
        return False
    return True
