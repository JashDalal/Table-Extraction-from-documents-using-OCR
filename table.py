import PIL.Image
import cv2
import pytesseract


image = cv2.imread(r'C:\Users\user\Desktop\Handwriting Recognition\Handwriting_recognition\table\scan_5-5.jpg',cv2.IMREAD_COLOR)
cv2.imshow('img', image)
cv2.waitKey(0)


grayedimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
grayedimg = cv2.threshold(grayedimg, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] 
cv2.imwrite(r"C:\Users\user\Desktop\Handwriting Recognition\Handwriting_recognition\table1.jpg", grayedimg)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# tabula-py is just a wrapper around tabula-java
text = pytesseract.image_to_string(PIL.Image.open(r"C:\Users\user\Desktop\Handwriting Recognition\Handwriting_recognition\table1.jpg"),lang='eng', config='--psm 3')
print(text)

