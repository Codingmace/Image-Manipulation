import os

def path(mypath):
    f = []
    for(dirName, subdirlist, fileList) in os.walk(mypath):
#         print('Found directory: %s' % dirName)
        for fname in fileList:
            if "jpeg" in fname or "JPEG" in fname or "jpg" in fname or "JPG" in fname or "png" in fname or "PNG" in fname:
                f.append(dirName + "\\" + fname)
#     print(f)
    return f

# path(".")
