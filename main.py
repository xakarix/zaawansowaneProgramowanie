import pytesseract
from PIL import Image
import cv2

pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"

print("1:", pytesseract.image_to_string(Image.open(r"images/text.jpg")))
print("###")

print(pytesseract.image_to_string(r"images/text.jpg"))

print(pytesseract.image_to_string(Image.open(r"images/text.jpg"), lang="eng"))
