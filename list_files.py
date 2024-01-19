from glob import glob

path = "/home/tim/Downloads/maries_filer/**/*.mov"

ret = glob(path, recursive=True)

print(len(ret))