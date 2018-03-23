from datetime import datetime
from CompLiscence import *
from dll1 import *
from walkpath import path

# Grab all the files
# Go one by one and compare (BATCH)
# If consecutive are same -> add into a gif
# After those are removed inspect the others
# (TESTING) copy to a folder all originals and their duplicates
# compare the rest and output to a folder a list of all duplicates
# Potential problem: May have some duplicates in this once compared. FIXED
# with Image.open(filepath) as img:
#     width, height = img.size
file = open("testfile.txt", "w")


def nextVal(n):
    q = True
    while(q):
        if n == None:
            q = False
        else:
            n = n.next
            if n == None:
                q = False
            else:
#                 print(str(n.data))
                file.write(str(n.data) + "\n")


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
#     ar = path("C:\\Users\\maste\\Dropbox\\Coding Projects\\Python\\Face Rec 1")
    ar = path(".")
#     ar = path("D:\\Photos Test\\Jacob iPhone 6 PNG")
#     ar = path("C:\\Users\\Admin\\Desktop\\Photos Test\\Jacob iPhone 6 PNG")
    print(datetime.now().time())
#     ar = path("D:\\Photos Test\\Hannah PNG")
#     print(datetime.now().time())
    dupar = []
    max = len(ar)
    print(max)
    ll = LinkedList()
    x = 0
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
                if iwa == iwb and iha == ihb:
                    if ib.mode == ia.mode:
                        if is_equal(ia, ib, .7):
                            percentage = image_diff_percent(ia, ib)
                            ll2.add(ar[y], percentage)
                            ar.remove(ar[y])
#                 Image.close(ib)
            y += 1
        ll.add(ll2, None)
        print(len(ar))
        print(datetime.now().time())
    while(len(ar) > 0):
        ll2 = LinkedList()
#         print(ar[0] + " q")
        ll2.add(ar[0], None)
        ar.remove(ar[0])
        ll.add(ll2, None)
    temper = ll.head
#     print(ll.size())
    while(temper != None):
        temper = nextVal(temper)
    file.close()
    print(datetime.now().time())

    
main()
