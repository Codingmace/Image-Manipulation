# Compares and prints Image difference percentage
from PIL import Image


image_a = Image.open("008 (2).JPG")
image_b = Image.open("00881.jpg")

# In CompLiscence.py File
percentage = image_diff_percent(image_a, image_b)
# percentage = image_diff_percent("008 (2).JPG", "00881.jpg")

print(percentage)
