# importing cv2 
import cv2 
import numpy as np
# path 
path = '04.jpg'
image = cv2.imread(path) 
ksize = (3, 3)
# boxFilter(src, dst, ddepth, ksize, anchor, normalize, borderType)
#Sriver para convertir a escala de grises
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(image,cv2.CV_64F ,  cv2.BORDER_DEFAULT)

cv2.imwrite('salida.jpg', laplacian)