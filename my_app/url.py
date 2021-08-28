from flask import Blueprint , render_template , request
import os
from Controller.utilities import cargaConfig , nameRandom

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
            file.save(os.getcwd() + configuration["general"][0]["Imagenes"]+id+file.filename)
            return "Imagen guardada"
        except FileNotFoundError:
            return "Folder no existe"
            print("Hola mundo")

    return "recibido"

