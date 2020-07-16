from pytesseract import image_to_string
import re
from PIL import Image
# import cv2
# import numpy as np

import os
# TODO below to store the data in Mongo dB
# from pymongo import MongoClient 

# construct the CLI argument parse and parse the arguments
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
# ap.add_argument("-r", "--reference", required=True,
	# help="path to reference MICR E-13B font")
args = vars(ap.parse_args())

inp_path = 'inputs/'
input_file_path = os.path.join(inp_path, args["image"] )
print('Trying to process ' + input_file_path + '\n')

img = Image.open(input_file_path)
ocr_text = image_to_string(img)

# print(ocr_text)

import time,calendar
localtime = time.asctime( time.localtime(time.time()) )
print(localtime)

# Open a file
output_file_path = "outputs/"
save_path = output_file_path #'C:/example/'

name_of_file = 'ocr_'+args["image"] #input("What is the name of the file: ")

completeName = os.path.join(save_path, name_of_file+".txt")  

print('Writing to ' + completeName + '\n')

fo = open(completeName, "a")
fo.write('\n\n\t'+localtime+'\n\n')
fo.write(ocr_text)
fo.write('\n')
fo.write('^EOF \n \n')
#os.rename("foo.txt","bar.txt")

# Close opend file
fo.close()

print(ocr_text.find('IFS') )
print(ocr_text.count('IFSC') )

ifsc_text = ocr_text

found_IFS = ifsc_text.find('IFS')

if found_IFS >0:
	print('SIVA ',ifsc_text.find('IFS') )
	ifsc_pattern = r"(IFS.*.[A-Z|a-z]{4}[0][\d]{6})"
	match_ifsc_pattern = re.search(ifsc_pattern, ifsc_text)
	print( match_ifsc_pattern.groups() )
	print( match_ifsc_pattern.group(1) )
	print( '\t~~~~~~~~~~~~~' )
else:
	print( '\tNOT FOUND~~~~~~~~~~~~~' )


# pythoon scripts an overview https://riptutorial.com/Download/python-language.pdf

# The IFSC is an 11-character code with the first four alphabetic characters representing the bank name, and the last six characters (usually numeric, but can be alphabetic) representing the branch. The fifth character is 0 (zero) and reserved for future use.
# REGEXP for IFSC is ([A-Z|a-z]{4}[0][\d]{6}) 

# Credits Wikipedia & RBI site & Razor pay API site

