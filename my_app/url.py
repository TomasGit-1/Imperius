from flask import Blueprint , render_template , request
import os
from Controller.utilities import cargaConfig , nameRandom
from Api.Imagen import Imagen

api_Imperius = Blueprint('api_Imperius' , __name__)
configuration = cargaConfig()

@api_Imperius.route("/")
def home():
    return render_template("home.html")


@api_Imperius.route("/imperius/")
def Home_App():
    return render_template("imperius.html")

@api_Imperius.route("/cargar_image", methods = ['POST'])
def cargar_image():
    id = nameRandom(5)
    if request.method == "POST":
        file = request.files['file']
        try:
            ruta_Img_Original = os.getcwd() + configuration["general"][0]["Imagenes"]+id+file.filename
            file.save(ruta_Img_Original)
            objImagen = Imagen()
            objImagen.Escala_Grises(ruta_Img_Original)
            return "Imagen guardada"
        except FileNotFoundError:
            return "Folder no existe"
            print("Hola mundo")

    return "recibido"

