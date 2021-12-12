import cv2

# Read the image.
img = cv2.imread('05.jpg')

# Apply bilateral filter with d = 15,
# sigmaColor = sigmaSpace = 75.
#ksize, sigma_color, sigma_space
bilateral = cv2.bilateralFilter(img, 5, 100, 100)

# Save the output.
cv2.imwrite('salida.jpg', bilateral)
