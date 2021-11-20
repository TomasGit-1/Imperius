#No se encuentra el metodo
# importing cv2 
import cv2 
# path 
path = '05.jpg'
image = cv2.imread(path) 
image = cv2.buildPyramid(image, 12 )
cv2.imwrite('salida.jpg', image)