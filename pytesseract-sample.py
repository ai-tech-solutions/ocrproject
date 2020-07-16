# https://github.com/madmaze/pytesseract
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

filename = 'CUB_CHQ.JPG'
filename1 = './inputs/AXIS_CHQ_1.jpg'
filename_eng = './inputs/HDFC_CTS.jpg'
filename_hin = './inputs/bilingual_eng_hindi.jpg'


# Simple image to string
print(pytesseract.image_to_string(Image.open(filename_eng)))

# French text image to string
# Hindi text image to string
print(pytesseract.image_to_string(Image.open(filename_hin), lang='hin'))

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
print(pytesseract.image_to_string(filename))

# Batch processing with a single file containing the list of multiple image file paths
# print(pytesseract.image_to_string('images.txt'))

# Timeout/terminate the tesseract job after a period of time
try:
    print(pytesseract.image_to_string(filename, timeout=2)) # Timeout after 2 seconds
    print(pytesseract.image_to_string(filename, timeout=0.5)) # Timeout after half a second
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    pass

# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open('./inputs/campdf.jpeg')))

# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(Image.open(filename1)))

# Get information about orientation and script detection
print(pytesseract.image_to_osd(Image.open(filename1)))

# Get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr(filename1, extension='pdf')
with open('test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default

# Get HOCR output
hocr = pytesseract.image_to_pdf_or_hocr(filename1, extension='hocr')
