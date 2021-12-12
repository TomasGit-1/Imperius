
# importing cv2 
import cv2 
# path 
path = '05.jpg'
image = cv2.imread(path) 
ksize = (10, 10)
# boxFilter(src, dst, ddepth, ksize, anchor, normalize, borderType)

image = cv2.boxFilter(image ,-1, ksize , True)
cv2.imwrite('salida.jpg', image)

# Displaying the image 
# cv2.imshow(window_name, image) 