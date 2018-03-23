from CompLiscence import *
from ll1 import *
from walkpath import *

# from LinkedList import *
# Grab all the files (BATCH)
# Go one by one and compare
# If consecutive are same -> add into a gif
# After those are removed inspect the others
# (TESTING) copy to a folder all originals and their duplicates
# compare the rest and output to a folder a list of all duplicates
# Potential problem: May have some duplicates in this once compared
# with Image.open(filepath) as img:
#     width, height = img.size


def main():
    ar = path(".")
    dupar = []
    max = len(ar)
    ll = LinkedList()
    for x in range(max - 1):
        ll2 = LinkedList()
#         n = Node(ar[x])
        ll2.add(ar[x])
        ll.add(ll2)
#         ll2.clear()
#         print("Here")
#     x. remove() # remove something from an array
#     print(ll.get(0))
#     for x in range(max - 1):
    for x in range(len(ar) - 1):
        ia = Image.open(ar[x])
        ll2 = LinkedList()
        ll2.add(ar[x])
        iwa, iha = ia.size
        for y in range(x + 1, max):
            ib = Image.open(ar[y])
            iwb, ihb = ib.size
    #         Different orientatino
    #         if iwa == ihb and iha == iwb: # Different orientation
    #             ib.rotate(90) # Flip the image once
            if iwa == iwb and iha == ihb:
                if is_equal(ia, ib, .7):
                    percentage = image_diff_percent(ia, ib)
                    print(ar[x] + " " + ar[y] + " " + (str((percentage))))
                    rem = ar[y]
                    ll2.add(ar[y])
                    ar.remove(rem)
#                     print((str(total_histogram_diff(pixel_diff(ia, ib)))))
                    dupar.append(ar[x] + " " + ar[y])
#             else:
#                 print("Incompatiable")
        ll.add(ll2)
    
main()
