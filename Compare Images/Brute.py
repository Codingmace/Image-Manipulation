from Old import *
from datetime import datetime
from send2trash import send2trash
from walkpath import path
import Image

# Imports all the images
# Using a 100% Check checking every pixel

file = open("testfile.txt", "w")


def nextNodes(n):
    temp = True
    while(temp):
        if n == None:
            temp = False
        else:
            n = n.next
            if n == None:
                temp = False
            else:
                file.write(str(n.data) + "\n")


# Test that the files are valid and compatbile
def same(a , b):
    if(".JPG" in a or ".jpg" in a):
        return ".JPG" in b or ".jpg" in b
    elif(".jpeg" in a or ".JPEG" in a):
        return ".jpeg" in b or ".JPEG" in b
    elif(".png" in a or ".PNG" in a):
        return ".png" in b or ".PNG" in b
    else:
        print("That is not a valid format")
        return False


def main():
    ar = path("D:\\Photos Test\\Jacob iPhone 6 JPG 1")
#     ar = path("D:\\cpy")
    print(datetime.now().time())
    print(len(ar))
    ll = LinkedList()
    x = 0
    cons = 0;
    while(len(ar) > 0):
        ia = Image.open(ar[x])
        ll2 = LinkedList()
        ll2.add(ar[x], None)
        ar.remove(ar[x])
        iwa, iha = ia.size
        y = 0
        while(y < len(ar)):
            if(same(str(ar[x]), str(ar[y]))):
                ib = Image.open(ar[y])
                iwb, ihb = ib.size
#                 if iwa == iwb and iha == ihb:
#                     if ib.mode == ia.mode:
#                         if is_equal(ia, ib, .7):
#                             percentage = image_diff_percent(ia, ib)
#                             if percentage == 0.0:
#                                 send2trash(ar[y])
#                             else:
#                                 ll2.add(ar[y], percentage)
#                             ar.remove(ar[y])
            
            y += 1
        ll.add(ll2, None)
        cons += 1
    while(len(ar) > 0):
        ll2 = LinkedList()
        ll2.add(ar[0], None)
        ar.remove(ar[0])
        ll.add(ll2, None)
    temper = ll.head
    while(temper != None):
        temper = nextNodes(temper)
    file.close()
    print(cons)
    print(datetime.now().time())
    
# main()
