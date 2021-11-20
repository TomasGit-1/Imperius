# importing cv2 
import cv2 
import numpy as np
# path 
path = '07.jpg'
image = cv2.imread(path) 
kernel = np.ones((5, 5), 'uint8')
# Numeros impares 
dilate_img = cv2.medianBlur(image,9)
cv2.imwrite('salida.jpg', dilate_img)