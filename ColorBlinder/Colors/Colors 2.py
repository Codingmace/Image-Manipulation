from datetime import datetime
from os import listdir, path 
from PIL import Image, ImageDraw


f = open("Colorblind Table.txt") # Filling Database

def readline():
    s = f.readline().strip()
    while(len(s) <= 0):
        s = f.readline().strip()
    return s

def match(a,b):
    R1 = a[0]
    G1 = a[1]
    B1 = a[2]
    R2 = R1 % 5
    G2 = G1 % 5
    B2 = B1 % 5
    R3 = 0
    G3 = 0
    B3 = 0
    if(R2 == 0):
        R3 = R1
    elif (R2 == 1):
        R3 = R1 - 1
    elif (R2 == 2):
        R3 = R1 - 2
    elif (R2 == 3):
        R3 = R1 + 2
    elif (R2 == 4):
        R3 = R1 + 1
    if(B2 == 0):
        B3 = B1
    elif (B2 == 1):
        B3 = B1 - 1
    elif (B2 == 2):
        B3 = B1 - 2
    elif (B2 == 3):
        B3 = B1 + 2
    elif (B2 == 4):
        B3 = B1 + 1
    if(G2 == 0):
        G3 = G1
    elif (G2 == 1):
        G3 = G1 - 1
    elif (G2 == 2):
        G3 = G1 - 2
    elif (G2 == 3):
        G3 = G1 + 2
    elif (G2 == 4):
        G3 = G1 + 1
    
    for i in range(len(b)):
        if(R3 == (int(b[i][0])) and G3 == (int(b[i][1])) and B3 == (int(b[i][2]))):
            return (int(b[i][3]), int(b[i][4]),int(b[i][5]))
    return (0,0,0)


def main():
    stdirs = "C:\\Users\\School\\Desktop\\Testers" # Starting Directory
    ar = listdir(stdirs)
    print(ar)
    print(datetime.now().time())
    print(len(ar))
    phcount = 0 # Photo Count
    cons = 0;
    
    # Reading in the chart conversions
    types = 3 # Normal, Protanopia, Deutanopia, Tritanoptia
    deut = [] # deuteranopia
    prot = [] # protanopia
    trit = [] # tritanopia
    s = f.readline() # Comments
    s = f.readline()
    while(not (s == "")):
        asp = s.strip().split(" ")
        type = asp[0] # What it is
        if(type == "deuteranopia"):
            asp.remove("deuteranopia")
            deut.append(asp)
        elif (type == "protanopia"):
            asp.remove("protanopia")
            prot.append(asp)
        elif (type == "tritanopia"):
            asp.remove("tritanopia")
            trit.append(asp)
        else:
            #That didn't work apparently
            print(type + " Doesn't exist yet")
        s = f.readline().strip()
    # Reading the file names

    while (phcount < len(ar) and phcount < 2):
        print(ar[phcount])
        photo = Image.open(stdirs + "\\" + ar[phcount]) #your image
      #  photo = photo.convert('RGB')
        width = photo.size[0] # define W and H
        height = photo.size[1]
        img = Image.new('RGB', (width, height), "black") # Create black image
        pixels = img.load() # Creates pixel map


        for y in range(0, height): #each pixel has coordinates
            row = ""
            for x in range(0, width): # Width
                RGB = photo.getpixel((x,y))
                R,G,B = RGB
                # Finding the Opposing one
                RGB2 = match([R,G,B], deut)

            #    print(RGB2)
                pixels[x,y] = RGB2

        phcount += 1
        img.save(stdirs + "\\thats\\" + str(phcount) + ".jpg")
main()
