try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def rectext(image):
    text = pytesseract.image_to_string(Image.open(image))
    return text
info = rectext('TEST1.jpg')
print(info)

#To save as a text file
# file = open('info.txt', 'w')
# file.write(info)
# file.close()
# print("Finished")