"""
import cv2
import pytesseract

filename = 'scan4-2cloumn.jpg'

# read the image and get the dimensions
img = cv2.imread(filename)
h, w, _ = img.shape # assumes color image

# run tesseract, returning the bounding boxes
boxes = pytesseract.image_to_boxes(img) # also include any config options you use
print(boxes.encode('utf8'))
# draw the bounding boxes on the image
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

# show annotated image and wait for keypress
#cv2.imshow(scan_3-1out, img)
scan4_2cloumn = 'scan4_2cloumn.jpg'
#img = cv2.imread(scan4_2cloumn)
cv2.imwrite (scan4_2cloumn, img)
#cv2.waitKey(0)

"""
import pytesseract
from pytesseract import Output
import cv2
img = cv2.imread('scan_1-1.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
#print(d.encode('utf8'))
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

tesseract_render_out = 'tesseract_render_out.jpg'
#img = cv2.imread(scan4_2cloumn)
cv2.imwrite (tesseract_render_out, img)
#img.save(fileout.jpg)
#cv2.waitKey(0)

"""
from PIL import Image
import pytesseract
image=pytesseract.image_to_data(Image.open('scan_1-1.jpg'))
"""