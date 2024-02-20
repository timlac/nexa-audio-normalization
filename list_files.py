from glob import glob
import os

from box_scripts.main_validation_study_filter import belongs_to_main_validation_study

path = "data/original_validation_experiment"

i = 0
for filename in os.listdir(path):
    i += 1

print(i)