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

# returns Value of next node if there is one
def nextVal(n):
    q = True
#     print(str(n.data))
    while(q):
        if n == None:
#             print(n.data)
            q = False
        else:
            n = n.next
            if n == None:
#                 quit
                q = False
            else:
                print(str(n.data))

def path(a):
    return {1,2,3}

def main():
    ar = path(".")
    dupar = []
    max = len(ar)
    ll = LinkedList()
    x = 0
    while(len(ar) > 0):
#     for x in range(len(ar) - 1):
        ia = Image.open(ar[x])
        ll2 = LinkedList()
        ll2.add(ar[x])
        iwa, iha = ia.size
        y = 1
        while(y < len(ar)):
#         for y in range(x + 1, len(ar) - 1):
#             print(str(x) + " "+ str(y) + " " + str(len(ar)))
            ib = Image.open(ar[y])
            iwb, ihb = ib.size
#         Different orientatino
#         if iwa == ihb and iha == iwb: # Different orientation
#             ib.rotate(90) # Flip the image once
            if iwa == iwb and iha == ihb:
                if is_equal(ia, ib, .7):
                    percentage = image_diff_percent(ia, ib)
#                     print(ar[x] + " " + ar[y] + " " + (str((percentage))))
#                     rem = ar[y]
                    ll2.add(ar[y])
                    ar.remove(ar[y])
#                     dupar.append(ar[x] + " " + ar[y])
#             else:
#                 print("Incompatiable")
            y += 1
        ll.add(ll2)
#         Removes x from the list
#         rem = ar[x]
#         ll2.add(ar[x])
#         ar.remove(rem)
        ar.remove(ar[x])
#         x = x+1
    while(not len(ar) == 0):
#         print(str(len(ar)))
        ll2 = LinkedList()
#         rem = ar[0]
        ll2.add(ar[0])
        ar.remove(ar[0])
        ll.add(ll2)
    print(ll.head.next.next.data)
    temper = ll.head
    while(temper != None):
        temper = nextVal(temper)
#         print(str(ll2))
#     while(ll):
#         print(ll)


main()
