
# Python program to explain cv2.blur() method 
# importing cv2 
import cv2 
# path 
path = '05.jpg'
# Reading an image in default mode 
image = cv2.imread(path) 
# Window name in which image is displayed 
window_name = 'Image'
# ksize
ksize = (10, 10)
# Using cv2.blur() method 
image = cv2.blur(image, ksize , -1) 
cv2.imwrite('salida.jpg', image)

# Displaying the image 
cv2.imshow(window_name, image) 