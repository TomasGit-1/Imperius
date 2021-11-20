
# importing cv2 
import cv2 
import numpy as np
# path 
path = '06.png'
image = cv2.imread(path) 
kernel = np.ones((5, 5), 'uint8')

img_erosion = cv2.erode(image,  kernel, iterations=1)
cv2.imwrite('salida.jpg', img_erosion)