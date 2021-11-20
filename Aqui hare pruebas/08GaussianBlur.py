
# importing cv2 
import cv2 
import numpy as np
# path 
path = '07.jpg'
image = cv2.imread(path) 
dilate_img = cv2.GaussianBlur(image, (5 ,5) , cv2.BORDER_DEFAULT)

cv2.imwrite('salida.jpg', dilate_img)