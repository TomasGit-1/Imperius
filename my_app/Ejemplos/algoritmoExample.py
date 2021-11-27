#Este es un ejemplod de como deben de cargar el algoritmo
#Ejemplo BilateralFilter
data = ["identificador" , 15 , 17]
d = int(data[1])
sigmaColor = sigmaSpace = float(data[2])
image = cv2.bilateralFilter(img , d , sigmaColor, sigmaSpace)
