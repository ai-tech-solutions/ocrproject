import cv2
import pytesseract
from pytesseract import Output

filename = 'CUB_CHQ.JPG'
filename = './inputs/HDFC_CTS.jpg'

# img = cv2.imread('invoice-sample.jpg')
img = cv2.imread(filename)

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())



# Credits : https://nanonets.com/blog/ocr-with-tesseract/
