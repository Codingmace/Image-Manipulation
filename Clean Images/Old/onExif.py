# Printing Exif to file. Fail

import exifread

path_name = "008 (2).JPG"
path = "0088.jpg"
# Open image file for reading (binary mode)
f = open(path_name, 'rb')
g = open(path, 'rb')

# Return Exif tags
tags = exifread.process_file(f)
tag = exifread.process_file(g)
print(tags)
print(tag)
h = open("g.txt", 'w')
i = open("v.txt", 'w')

h.write(tags)
# print >> h, tags
print >> i, tag
