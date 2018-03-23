from PIL import Image
from PIL.ExifTags import TAGS
import piexif
#import os
filename = "Test (3).jpg"
new_file = "img\\Test (3)s.jpg"

# Transfers the Exif
def getOn(filename, new_file):
    im = Image.open(filename)
    exif_dict = piexif.load(im.info["exif"])
    exif_bytes = piexif.dump(exif_dict)
    im.save(new_file, "jpeg", exif=exif_bytes)

# Returns Exif Data (Used for printing)
def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


#os.makedirs("img") # need to add if already exist statement
#getOn(filename, new_file)
getOn("0 e.jpg", "img\\0e.jpg")
#getOn("qsd.jpg", "img\\qss.jpg");
#print(get_exif(new_file))

