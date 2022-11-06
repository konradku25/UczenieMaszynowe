import pytesseract
import cv2
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def img_text(img_str):
    img = cv2.imread(img_str)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(pytesseract.image_to_string(img_gray))


img_text("images\\img1.png")
img_text("images\\img2.png")
img_text("images\\img3.png")
img_text("images\\img4.png")
img_text("images\\img5.png")
