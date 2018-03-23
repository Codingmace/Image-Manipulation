# Same as Comp1 really. Compares 2 and prints percentage and equal by 1
from PIL import Image
from CompLiscence import *

def main(): 
#     image_a = Image.open("qsd.JPG")
#     image_b = Image.open("qsd2s.jpg")
    image_a = Image.open("Lenna100.jpg")
    image_b = Image.open("Lenna50.jpg")
#     image_b = Image.open("0 e.jpg")
    percentage = image_diff_percent(image_a, image_b)
    # percentage = image_diff_percent("008 (2).JPG", "00881.jpg")
    print(percentage)
    print(is_equal(image_a, image_b, 1))

main()