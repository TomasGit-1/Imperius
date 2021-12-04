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

    encodeData = []

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

    def ImagenWrite(self  , image):
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

    
    def setEncodeImg(self , data=[]):
        self.encodeData = []
        self.encodeData = data

    def getEncodeImg(self):
        return self.encodeData[0] , self.encodeData[1]

    


    #=================================================#
    #=================================================#
    #                Operadores                       #
    #=================================================#
    #=================================================#

    def FiltroUser(self, path):
        img = self.ImagenRead(self.getImg_ruta())
        data = []
        image_64_encode =0
        ruta_img = 0
        image =""
        code=""

        with open(path, 'r') as f:
            lineas = f.readlines()

        for line in lineas:
            exec(code)
            #eval(code)
        #    code= code +line
        #exec(open(path).read())
        print("")

        image_64_encode , ruta_img = self.ImagenWrite(image)
        self.setEncodeImg([image_64_encode , ruta_img])

        #==============================#


    def Escala_Grises(self , data=[]):
        try:
            img = self.ImagenRead(self.getImg_ruta())
            image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            image_64_encode , ruta_img = self.ImagenWrite(image)
            self.setEncodeImg([image_64_encode , ruta_img])
            # return image_64_encode , ruta_img
        except Exception as e:
            print(str(e))

    #================================================#
    #                   Blur                         #
    #================================================#
    def Blur(self , ruta):
        try:
            #ksize puede tomar diferentes valores ksize = (30 , 30)
            img = self.ImagenRead(self.getImg_ruta())
            # Aplicar filtro de desenfoque
            ksize = (30, 30)
            image = cv2.blur(img, ksize , cv2.BORDER_DEFAULT) 
            image_64_encode , ruta_img = self.ImagenWrite(image)
            self.setEncodeImg([image_64_encode , ruta_img])
        except Exception as e:
            print(str(e))

    #================================================#
    #                   bilateralFilter              #
    #================================================#
    def Bilateral_Filter(self, data=[]):
        img = self.ImagenRead(self.getImg_ruta())
        # d , sigma_space , sigma_color
        # Apply bilateral filter with d = 15,
        # sigmaColor = sigmaSpace = 75.
        #ksize, sigma_color, sigma_space
        #bilateral = cv2.bilateralFilter(img, 5, 100, 100)
        d = int(data[1])
        sigmaColor = sigmaSpace = float(data[2])
        image = cv2.bilateralFilter(img , d , sigmaColor, sigmaSpace)
        image_64_encode , ruta_img = self.ImagenWrite(image)
        self.setEncodeImg([image_64_encode , ruta_img])
    
    #================================================#
    #                   BoxFilter                    #
    #================================================#
    def Box_Filter(self, data=[]):
        img = self.ImagenRead(self.getImg_ruta())
        ksize = (10, 10)
        # boxFilter(src, dst, ddepth, ksize, anchor, normalize, borderType)
        image = cv2.boxFilter(img ,-1, ksize)
        image_64_encode , ruta_img = self.ImagenWrite(image)
        self.setEncodeImg([image_64_encode , ruta_img])

    #================================================#
    #                   Dilate                       #
    #================================================#
    def Dilate(self, data=[]):
        img = self.ImagenRead(self.getImg_ruta())
        kernel = np.ones((5, 5), 'uint8')
        image = cv2.dilate(img, kernel, iterations=1)        
        image_64_encode , ruta_img = self.ImagenWrite(image)
        self.setEncodeImg([image_64_encode , ruta_img])

    #================================================#
    #                   Erode                        #
    #================================================#
    def Erode(self, data=[]):
        img = self.ImagenRead(self.getImg_ruta())
        kernel = np.ones((5, 5), 'uint8')
        image = cv2.erode(img,  kernel, iterations=1)
        image_64_encode , ruta_img = self.ImagenWrite(image)
        self.setEncodeImg([image_64_encode , ruta_img])

    #================================================#
    #                   filter2D                     #
    #================================================#
    def Filter2D(self, data=[]):
        img = self.ImagenRead(self.getImg_ruta())
        kernel = np.ones((5, 5), 'uint8')

        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ])

        image = cv2.filter2D(img, cv2.CV_64F,kernel)

        image_64_encode , ruta_img = self.ImagenWrite(image)
        self.setEncodeImg([image_64_encode , ruta_img])

    #================================================#
    #                   GaussianBlur                 #
    #================================================#
    def GaussianBlur(self, data=[]):
        img = self.ImagenRead(self.getImg_ruta())
        image = cv2.GaussianBlur(img, (5 ,5) , cv2.BORDER_DEFAULT)
        image_64_encode , ruta_img = self.ImagenWrite(image)
        self.setEncodeImg([image_64_encode , ruta_img])

    
    #================================================#
    #                   Laplacian                    #
    #================================================#
    def Laplacian(self, data=[]):
        img = self.ImagenRead(self.getImg_ruta())
        image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        image = cv2.Laplacian(image,cv2.CV_64F ,cv2.BORDER_DEFAULT)
        image_64_encode , ruta_img = self.ImagenWrite(image)
        self.setEncodeImg([image_64_encode , ruta_img])

    #================================================#
    #                   MedianBlur                   #
    #================================================#
    def MedianBlur(self, data=[]):
        img = self.ImagenRead(self.getImg_ruta())
        # Numeros impares 
        image = cv2.medianBlur(img,9)
        image_64_encode , ruta_img = self.ImagenWrite(image)
        self.setEncodeImg([image_64_encode , ruta_img])

    #================================================#
    #                   Sobel                        #
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
    

    #def Filtros(self , data=[]):

    #Nombre de la funcion(operador)
    #Parametros (tIPOS DE DATOS)
    #Codigo de la funcion

    #def filtro50([parametros]):
        #print("Hola mundo")
        #print("Aqui porceso la imagen")


        #     precio = 5
# cadenas = ['(4+5)**2',
#            '(1, 2, 3)',
#            '["I", "II", "III"]',
#            '{"a":1, "b":2, "c":3}',
#            'len("Python")',
#            '20 * precio',
#            '__import__("platform").python_version()']

# for cadena in cadenas:
#     print(cadena, "=>", eval(cadena), 
#           "Tipo:",type(eval(cadena)))


    #================================================#
    #                   Usuario                        #
    #================================================#
    def Sobel_CSAAJel6(self, data=[]):
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

    #================================================#
    #                   Usuario                        #
    #================================================#
    def Sobel_2LEUlCk2(self, data=[]):
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
