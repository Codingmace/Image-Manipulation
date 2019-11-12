from datetime import datetime
from os import listdir, path 
from PIL import Image, ImageDraw
#import numpy as np


# import os
# from walkpath import path
#import image
# import Image

# Imports all the images
# Using a 100% Check checking every pixel

file = open("testfile.txt", "w")
f = open("Table.txt") # Filling Database

def readline():
    s = f.readline().strip()
    while(len(s) <= 0):
        s = f.readline().strip()
    return s

def match(a,b):
    for i in range(len(b)):
        if(a[0] == b[i][0] and a[1] == b[i][1] and a[2] == b[i][2]):
          #  print("I GOT ONE")
            return i
    return -1

def repl(a , b):
    if(a < 0):
    #    print("SHIT THAT DOESN'T WORK")
        return (0,0,0);
    else:
        q = b[a]
        return (q[0], q[1] , q[2])

def main():
    stdirs = "C:\\Users\\School\\Desktop\\Testers" # Starting Directory
    ar = listdir(stdirs)
    print(datetime.now().time())
    print(len(ar))
    phcount = 0 # Photo Count
    cons = 0;
    
    # Reading in the chart conversions
    types = 4 # Normal, Protanopia, Deutanopia, Tritanoptia
    normrgb = [] # Normal RGB
    normhex = [] # Normal Hex
    protrgb = [] # Protanopia RGB
    prothex = [] # Protanopia Hex
    deutrgb = [] # Deutanopia RGB
    deuthex = [] # Deutanopia Hex
    tritrgb = [] # Tritanoptia RGB
    trithex = [] # Tritanoptia Hex
    s = readline() #TABLE 1
    s = readline()
#    print("1 " +s)
#    print("2 " +f.readline().strip())
#    print("3 " +f.readline())
    con = 0 # Counter for arrays
    conh = 0 # Counter for hex
    while("Table" not in s):
        s = s.strip()
       # print(s)
        if(s == "table"): # Use to be blank Line 
            print("IGNORED")
        else:
           # s = f.readline()
            atmp = s.split(" ")
            if (len(atmp) == 3):
                normrgb.append([int(atmp[0]), int(atmp[1]),int(atmp[2])])
#                normrgb.append(int(atmp[1]))
#                normrgb.append(int(atmp[2]))
                
                s = readline()
                atmp = s.split(" ")
                protrgb.append([int(atmp[0]), int(atmp[1]),int(atmp[2])])
            #    protrgb.append(int(atmp[1]))
           #     protrgb.append(int(atmp[2]))

                s = readline()
                atmp = s.split(" ")
                deutrgb.append([int(atmp[0]), int(atmp[1]),int(atmp[2])])
             #   deutrgb.append(int(atmp[1]))
            #    deutrgb.append(int(atmp[2]))              
            
                s = readline()
                atmp = s.split(" ")
                tritrgb.append([int(atmp[0]), int(atmp[1]),int(atmp[2])])
         #       tritrgb.append(int(atmp[1]))
          #      tritrgb.append(int(atmp[2]))
                con += 3
                s = readline()
            elif ("#" in s):
                normhex.append(s)
                s = readline()
                prothex.append(s)
                s = readline()
                deuthex.append(s)
                s = readline()
                trithex.append(s)
                s = readline()
            else:
                s = readline()

#            print(len(atmp));
           # break
#    print(len(normr))
    # Reading the file names
   # print("MADE IT HERE")
    while (phcount < len(ar) and phcount < 1):
        print(ar[phcount])
        photo = Image.open(stdirs + "\\" + ar[phcount]) #your image
      #  photo = photo.convert('RGB')
        width = photo.size[0] #define W and H
        height = photo.size[1]
        img = Image.new('RGB', (width, height), "black") # Create black image
        pixels = img.load() # Creates pixel map
      #  print(width)
      #  print(height)

       # arrs = np.array(photo)
    #    print(arrs[0:10])
 #       width = 1
#        height = 1

        for y in range(0, 100): #each pixel has coordinates
            row = ""
            for x in range(0, 100): # Width
                RGB = photo.getpixel((x,y))
                R,G,B = RGB
                RGB2 = repl(match([R,G,B], normrgb),deutrgb)
           #     print(x)
           #     print(y)
                print(RGB2)
                pixels[x,y] = RGB2
                #print(R)
               # print(G)
               # print(B)
        # Testing to see what type they are going to do
        # Reading and creating new image (OPTIONAL TO MERGE THEM TOGETHER)
        # Print out and move to the next image
        phcount += 1

        img.save(stdirs + "\\thats\\" + ar[phcount])
main()
