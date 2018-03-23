from PIL import Image
from PIL.ExifTags import TAGS
import os
import piexif
import ntpath
from walkpath import path

# filename = "img/Test (1).jpg"
directory = "C:\\Users\\maste\\Dropbox\\Photos\\IPhone 6"

# Strips to filename
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def getOn(filename):
    new_file = directory + "/" + path_leaf(filename)
    im = Image.open(filename)
    exif_dict = piexif.load(im.info["exif"])
    exif_bytes = piexif.dump(exif_dict)
    im.save(new_file, "jpeg", exif=exif_bytes)
    print(filename + " worked")
    im.close()

def main():
    qr = []
    if not os.path.exists(directory):
        os.makedirs(directory)
    ar= path(directory + "\\testFolder");
    print(ar)
    for file in ar:
        if not os.path.exists(directory + "/"+ file):
            try:
                getOn(file)
            except:
                qr += file + "\n"
                print(file + " Doesn't Like you")
    file = open("dont.txt" , "w")
    for name in qr:
        file.write(name)
    file.close()
    
main()