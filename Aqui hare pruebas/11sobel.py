
import cv2
import numpy as np
img=cv2.imread("05.jpg")
# Calculation of Sobelx
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

x = cv2.Sobel(gray, cv2.CV_64F, 1,0, ksize=3, scale=1)
y = cv2.Sobel(gray, cv2.CV_64F, 0,1, ksize=3, scale=1)

absx= cv2.convertScaleAbs(x)
absy = cv2.convertScaleAbs(y)
edge = cv2.addWeighted(absx, 0.5, absy, 0.5,0)

cv2.imwrite('salida.jpg' , edge)