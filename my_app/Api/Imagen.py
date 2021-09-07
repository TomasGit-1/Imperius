from PIL import Image
from Controller.utilities import cargaConfig , nameRandom
import os
import base64 

class Imagen():
    
    configuration = cargaConfig()
    urls =["cargar_image" , "escala_grises"]
    registro = []

    def setImg_Original(self, ruta):
        self.registro = []
        self.registro.append([self.urls[0],ruta])

    def getImg_Original(self):
        return self.registro[0][1]

    def getRegistro(self):
        return self.registro

    def Escala_Grises(self , ruta):
        try:
            id = nameRandom(5)
            img = Image.open(ruta)
            ruta_img_escala_grises = os.getcwd() + self.configuration["general"][0]["Imagenes"]+id+".jpg"
            imgGray = img.convert('L')
            imgGray.save(ruta_img_escala_grises)
            self.registro.append([self.urls[1],ruta_img_escala_grises])
            image_64_encode = self.Base64(ruta_img_escala_grises)
            return image_64_encode
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

