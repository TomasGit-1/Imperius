    #================================================#
    #                   Usuario                        #
    #================================================#
    def Sobel(self, data=[]):
        img = self.ImagenRead(self.getImg_ruta())
        
        # Numeros impares 
        # Calculation of Sobelx
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        x = cv2.Sobel(gray, cv2.CV_64F, 1,0, ksize=3, scale=1)
        y = cv2.Sobel(gray, cv2.CV_64F, 0,1, ksize=3, scale=1)

        absx= cv2.convertScaleAbs(x)
        absy = cv2.convertScaleAbs(y)
        image = cv2.addWeighted(absx, 0.5, absy, 0.5,0)
        
        image_64_encode , ruta_img = self.ImagenWrite(image)
        self.setEncodeImg([image_64_encode , ruta_img])