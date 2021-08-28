from PIL import Image
from Controller.utilities import cargaConfig , nameRandom
import os

class Imagen():
    configuration = cargaConfig()
    def Escala_Grises(self , ruta):
        try:
            id = nameRandom(5)
            img = Image.open(ruta)
            imgGray = img.convert('L')
            imgGray.save(os.getcwd() + self.configuration["general"][0]["Imagenes"]+id+".jpg")
            print(os.getcwd() + self.configuration["general"][0]["Imagenes"]+id+".jpg")
        except Exception as e:
            print(str(e))