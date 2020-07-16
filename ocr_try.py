from pytesseract import image_to_string
import re
from PIL import Image
# import cv2
# import numpy as np

# inp = (input('Provide an input\t'))

img = Image.open("CUB_CHQ.JPG")
width, height = img.size
new_size = width*6, height*6
img = img.resize(new_size, Image.ANTIALIAS)
img = img.convert('L')
abc = img.point(lambda x: 0 if x < 170 else 300, '1')
print(image_to_string(abc))
