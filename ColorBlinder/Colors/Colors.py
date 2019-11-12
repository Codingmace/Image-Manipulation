from datetime import datetime
from os import listdir
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

def main():
    ar = listdir("C:\\Users\\School\\Desktop\\Testers")
    print(datetime.now().time())
    print(len(ar))
    x = 0
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
        print(s)
        if(s == "table"): # Use to be blank Line 
            print("IGNORED")
        else:
           # s = f.readline()
            atmp = s.split(" ")
            if (len(atmp) == 3):
                normrgb.append(int(atmp[0]))
                normrgb.append(int(atmp[1]))
                normrgb.append(int(atmp[2]))
                
                s = readline()
                atmp = s.split(" ")
                protrgb.append(int(atmp[0]))
                protrgb.append(int(atmp[1]))
                protrgb.append(int(atmp[2]))

                s = readline()
                atmp = s.split(" ")
                deutrgb.append(int(atmp[0]))
                deutrgb.append(int(atmp[1]))
                deutrgb.append(int(atmp[2]))              
            
                s = readline()
                atmp = s.split(" ")
                tritrgb.append(int(atmp[0]))
                tritrgb.append(int(atmp[1]))
                tritrgb.append(int(atmp[2]))
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
    print("MADE IT HERE")
    while (x < len(ar)):
        print(ar[x])

        
        # Testing to see what type they are going to do
        # Reading and creating new image (OPTIONAL TO MERGE THEM TOGETHER)
        # Print out and move to the next image
        x += 1
        
main()
