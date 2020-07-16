try:  
    from PIL import Image
except ImportError:  
    import Image
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\hamadasi\AppData\Local\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

filename = 'CUB_CHQ.JPG'
filename = './inputs/HDFC_CTS.jpg'

def ocr_core(filename = None):
    if filename is None:
        #filename = 'D:\Python screenshot\Deepfieldglass.png'
        return "file name is null"
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    textfile = open(r"HDFC_CTS.txt","w+")
    textfile.write(text)
    # return text.encode("utf-8")
    return "Successful"

print(ocr_core(filename))
'''
img = Image.open(input_file_path)
width, height = img.size
new_size = width*6, height*6
img = img.resize(new_size, Image.ANTIALIAS)
img = img.convert('L')
abc = img.point(lambda x: 0 if x < 170 else 300, '1')
ocr_text = image_to_string(abc)
'''
