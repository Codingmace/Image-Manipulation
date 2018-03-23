from PIL import Image
from PIL.ExifTags import TAGS
import piexif
from Default.exifcopy import get_exif

filename = "Test (3).jpg"
new_file = "Test (3)s.jpg"

# Transfers the Exif
def getOn(filename, new_file):
    im = Image.open(filename)
    exif_dict = piexif.load(im.info["exif"])
    # process im and exif_dict...
  #  w, h = im.size
 #   exif_dict["0th"][piexif.ImageIFD.XResolution] = (w, 1)
#    exif_dict["0th"][piexif.ImageIFD.YResolution] = (h, 1)
    exif_bytes = piexif.dump(exif_dict)
    im.save(new_file, "jpeg", exif=exif_bytes)
    
    # Prints out the tag
    for ifd in ("0th", "Exif", "GPS", "1st"):
        for tag in exif_dict[ifd]:
            xq = piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag]
            xx = piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag]
            print(xq)

# Returns Exif Data (Used for printing)
def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


print(get_exif(filename))
getOn(filename, new_file)
print(get_exif(new_file))
# print(get_exif(filename).__eq__(get_exif(new_file)))

