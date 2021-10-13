from PIL import Image ,  ImageFilter
from Controller.utilities import cargaConfig , nameRandom
import os
import base64 

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


    def Escala_Grises(self , ruta):
        try:
            id = nameRandom(5)
            img = Image.open(ruta)
            ruta_img_escala_grises = os.getcwd() + self.configuration["general"][0]["Imagenes"]+id+".jpg"
            imgGray = img.convert('L')
            imgGray.save(ruta_img_escala_grises)
            image_64_encode = self.Base64(ruta_img_escala_grises)
            return image_64_encode , ruta_img_escala_grises
        except Exception as e:
            print(str(e))

    def detectar_bordes(self , ruta):
        try:
            id = nameRandom(5)
            image = Image.open(ruta)
            ruta_img = os.getcwd() + self.configuration["general"][0]["Imagenes"]+id+".jpg"
            image = image.convert("L")
            image = image.filter(ImageFilter.FIND_EDGES)
            image.save(ruta_img)
            image_64_encode = self.Base64(ruta_img)
            return image_64_encode , ruta_img
        except Exception as e:
            print(str(e))

    def rotar_imagen(self , ruta):
        try:
            id = nameRandom(5)
            image = Image.open(ruta)
            ruta_img = os.getcwd() + self.configuration["general"][0]["Imagenes"]+id+".jpg"
            image = image.rotate(180) 
            image.save(ruta_img)
            image_64_encode = self.Base64(ruta_img)
            return image_64_encode , ruta_img
        except Exception as e:
            print(str(e))

    def blur_imagen(self , ruta):
        try:
            id = nameRandom(5)
            image = Image.open(ruta)
            ruta_img = os.getcwd() + self.configuration["general"][0]["Imagenes"]+id+".jpg"
            # Abra un archivo de imagen jpg, tenga en cuenta la ruta actual:
            image = Image.open(ruta)
            # Aplicar filtro de desenfoque:
            image = image.filter(ImageFilter.BLUR)
            image.save(ruta_img)

            image_64_encode = self.Base64(ruta_img)
            return image_64_encode , ruta_img
        except Exception as e:
            print(str(e))

    def Base64(self , ruta):
        try:
            image_64_encode =""
            with open(ruta, "rb") as image_file:
                image_64_encode = base64.b64encode(image_file.read()).decode('utf-8')
            image_64_encode = "<img src='data:image/png;base64,{}' class='img-thumbnail rounded mx-auto d-block' style='height:400px'>".format(image_64_encode)
            return image_64_encode
        except Exception as e:
            print(str(e))

    


