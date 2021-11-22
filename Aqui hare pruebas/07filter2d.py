# importing cv2 
import cv2 
import numpy as np
# path 
path = '07.jpg'
image = cv2.imread(path) 
'''
    [ 1 , 1,  1 , 1 , 1]
    [ 1 , 1,  1 , 1 , 1]
    [ 1 , 1,  1 , 1 , 1]
    [ 1 , 1,  1 , 1 , 1]
    [ 1 , 1,  1 , 1 , 1]
'''

kernel = np.ones((5, 5), 'uint8')

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

dilate_img = cv2.filter2D(image, cv2.CV_64F,kernel)

cv2.imwrite('salida.jpg', dilate_img)