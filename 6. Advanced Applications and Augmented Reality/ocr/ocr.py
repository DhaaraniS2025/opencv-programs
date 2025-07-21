import pytesseract as tess
from PIL import Image

# Set the path to the tesseract executable
tess.pytesseract.tesseract_cmd = r"C:\Users\Dhaarani S\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Load the image
img = Image.open(r"C:\Users\Dhaarani S\Desktop\ocr_detection\ocr_image1.png")
text = tess.image_to_string(img)

print(text)
