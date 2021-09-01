from flask import Blueprint , render_template , request
import os
from Controller.utilities import cargaConfig , nameRandom
from Api.Imagen import Imagen

api_Imperius = Blueprint('api_Imperius' , __name__)
configuration = cargaConfig()
__ruta_Img_Original =""
objImagen = Imagen()

@api_Imperius.route("/")
def home():
    return render_template("home.html")


@api_Imperius.route("/imperius/")
def Home_App():
    return render_template("imperius.html")

@api_Imperius.route("/cargar_image", methods = ['POST'])
def cargar_image():
    __ruta_Img_Original = ""
    id = nameRandom(5)
    if request.method == "POST":
        file = request.files['file']
        try:
            __ruta_Img_Original = os.getcwd() + configuration["general"][0]["Imagenes"]+id+file.filename
            file.save(__ruta_Img_Original)
            image_64_encode = objImagen.Base64(__ruta_Img_Original)
            return {"img_Orginal" : image_64_encode}
        except FileNotFoundError:
            return "Folder no existe"
            print("Hola mundo")

    return "recibido"

def Escala_Grises():
    objImagen = Imagen()
    objImagen.Escala_Grises(__ruta_Img_Original)


