from Controller.utilities import cargaConfig , nameRandom
import os
import base64
import cv2
import numpy as np

class Imagen():
    configuration = cargaConfig()
    urls =["cargar_image" , "escala_grises"]
    ruta_original ,ruta , metodo = "" , "" , ""
    identificador=""
    modelo = []
    modeloFinal = []

    def setDatos (self , datos = []):
        self.ruta = datos[0]
        self.identificador = datos[1]
        self.metodo = datos[2]
    
    def setImg_ruta(self , ruta):
        self.ruta_original = ruta

    def getImg_ruta(self):
        return self.ruta_original

    def LimpiarMemoria(self):
        self.modelo = []
        self.identificador = []
        self.ruta = []

    def LimpiarModelo(self):
        self.modeloFinal = []

    def Eliminar(self , pos):
        self.modeloFinal.pop(pos)
        return self.modeloFinal
    
    def getModelo(self):
        try:
            self.modelo.append([ "identificador",self.identificador])
            self.modelo.append([ "archivo"      ,self.ruta])
            self.modelo.append([ "algoritmo"    ,"Ninguno"])
            self.modelo.append([ "metodo"       ,self.metodo])
            return self.modelo
        except Exception as e:
            print (str(e))
    
    def getModeloFinal(self , datos):
        self.modeloFinal.append(datos)
        return self.modeloFinal

    def ImagenRead(self , ruta):
        # Read the image.
        img = cv2.imread(ruta)
        return img

    def ImagenWrite(self  , image ):
        id = nameRandom(5)
        ruta_img = os.getcwd() + self.configuration["general"][0]["Imagenes"]+id+".jpg"
        cv2.imwrite(ruta_img, image)
        image_64_encode = self.Base64(ruta_img)
        return image_64_encode , ruta_img

    def Base64(self , ruta):
        try:
            image_64_encode =""
            with open(ruta, "rb") as image_file:
                image_64_encode = base64.b64encode(image_file.read()).decode('utf-8')
            image_64_encode = "<img src='data:image/png;base64,{}' class='img-thumbnail rounded mx-auto d-block' style='height:400px'>".format(image_64_encode)
            return image_64_encode
        except Exception as e:
            print(str(e))


    #=================================================#
    #=================================================#
    #                Operadores                       #
    #=================================================#
    #=================================================#
    def Escala_Grises(self , data=[]):
        try:
            img = self.ImagenRead(self.getImg_ruta())
            image = img.convert('L')
            image_64_encode , ruta_img = self.ImagenWrite(image)
            return image_64_encode , ruta_img
        except Exception as e:
            print(str(e))

    def Blur(self , ruta):
        try:
            #ksize puede tomar diferentes valores ksize = (30 , 30)
            img = self.ImagenRead(self.getImg_ruta())
            # Aplicar filtro de desenfoque
            ksize = (30, 30)
            image = cv2.blur(img, ksize , cv2.BORDER_DEFAULT) 
            image_64_encode , ruta_img = self.ImagenWrite(image)
            return image_64_encode , ruta_img
        except Exception as e:
            print(str(e))

    def Bilateral_Filter(self, data=[]):
        img = self.ImagenRead(self.getImg_ruta())
        #================================================#
        #                   bilateralFilter              #
        #================================================#
        # d , sigma_space , sigma_color
        # Apply bilateral filter with d = 15,
        # sigmaColor = sigmaSpace = 75.
        #ksize, sigma_color, sigma_space
        #bilateral = cv2.bilateralFilter(img, 5, 100, 100)
        d = int(data[0])
        sigmaColor = sigmaSpace = float(data[1])
        image = cv2.bilateralFilter(img , d , sigmaColor, sigmaSpace)
        image_64_encode , ruta_img = self.ImagenWrite(image)
        return image_64_encode , ruta_img
    
    def Box_Filter(self, data=[]):
        img = self.ImagenRead(self.getImg_ruta())
        #================================================#
        #                   BoxFilter                    #
        #================================================#
        ksize = (10, 10)
        # boxFilter(src, dst, ddepth, ksize, anchor, normalize, borderType)
        image = cv2.boxFilter(img ,-1, ksize)
        image_64_encode , ruta_img = self.ImagenWrite(image)
        return image_64_encode , ruta_img

    def Dilate(self, data=[]):
        img = self.ImagenRead(self.getImg_ruta())
        #================================================#
        #                   Dilate                       #
        #================================================#
        kernel = np.ones((5, 5), 'uint8')
        image = cv2.dilate(img, kernel, iterations=1)        
        image_64_encode , ruta_img = self.ImagenWrite(image)
        return image_64_encode , ruta_img

    def Erode(self, data=[]):
        img = self.ImagenRead(self.getImg_ruta())
        #================================================#
        #                   BoxFilter                    #
        #================================================#
        kernel = np.ones((5, 5), 'uint8')
        image = cv2.Erode(img,  kernel, iterations=1)
        image_64_encode , ruta_img = self.ImagenWrite(image)
        return image_64_encode , ruta_img




