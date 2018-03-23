# Creates copy of clean Exif file
from PIL import Image
from PIL.ExifTags import TAGS
import os
import piexif
import ntpath

filename = "img/Test (1).jpg"
# new_file = "Test (1)s.png" # Doesn't create Image

# Strips to filename
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

# def getOn(filename, new_file):
def getOn(filename):
    directory = "cpy"
    if not os.path.exists(directory):
        os.makedirs(directory)
#     print(path_leaf(filename))
    new_file = directory + "/" + path_leaf(filename)
#     if("jpg" in filename):
    im = Image.open(filename)
    exif_dict = piexif.load(im.info["exif"])
    exif_bytes = piexif.dump(exif_dict)
    im.save(new_file, "jpeg", exif=exif_bytes)

# getOn(filename, new_file)
getOn(filename)
