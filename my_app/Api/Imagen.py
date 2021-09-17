from PIL import Image
from Controller.utilities import cargaConfig , nameRandom
import os
import base64 

class Imagen():
    configuration = cargaConfig()
    urls =["cargar_image" , "escala_grises"]
    ruta , metodo = "" , ""
    identificador=""
    modelo =[]

    def setImg_ruta(self, ruta):
        self.ruta = ruta
    def getImg_ruta(self):
        return self.ruta

    def setIdentificador(self , identificador):
        self.identificador = identificador
    
    def setMetodo(self , metodo):
        self.metodo = metodo
    
    def getModelo(self):
        self.modelo.clear()
        self.modelo.append({ "identificador" : ":"+self.identificador})
        self.modelo.append({ "archivo" : ":"+self.ruta})
        self.modelo.append({ "algoritmo" :":Ninguno"})
        self.modelo.append({ "metodo" : ":"+self.metodo})
        return self.modelo

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

    def Base64(self , ruta):
        try:
            image_64_encode =""
            with open(ruta, "rb") as image_file:
                image_64_encode = base64.b64encode(image_file.read()).decode('utf-8')
            image_64_encode = "<img src='data:image/png;base64,{}' class='img-thumbnail rounded mx-auto d-block' style='height:400px'>".format(image_64_encode)
            return image_64_encode
        except Exception as e:
            print(str(e))

    


