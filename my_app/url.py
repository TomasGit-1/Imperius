from flask import Blueprint , render_template , request
import os

api_Imperius = Blueprint('api_Imperius' , __name__)


@api_Imperius.route("/")
def home():
    return render_template("home.html")


@api_Imperius.route("/imperius/")
def Home_App():
    return render_template("imperius.html")

@api_Imperius.route("/cargar_image", methods = ['POST'])
def cargar_image():
    if request.method == "POST":
        file = request.files['file']
        try:
            file.save(os.getcwd() + "/my_app/images/" + file.name)
            return "Imagen guardada"
        except FileNotFoundError:
            return "Folder no existe"
            print("Hola mundo")

    return "recibido"

