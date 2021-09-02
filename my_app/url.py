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
        try:
            file = request.files['file']
            __ruta_Img_Original = os.getcwd() + configuration["general"][0]["Imagenes"]
            if not os.path.exists(__ruta_Img_Original):
                os.mkdir(__ruta_Img_Original)
            __ruta_Img_Original = __ruta_Img_Original + id+file.filename
            file.save(__ruta_Img_Original)
            objImagen.setImg_Original(__ruta_Img_Original)
            image_64_encode = objImagen.Base64(__ruta_Img_Original)
            return {"img_Orginal" : image_64_encode}
        except FileNotFoundError:
            return "Folder no existe"
        except Exception as e:
            print(str(e))

@api_Imperius.route("/escala_grises" , methods = ['POST'])
def Escala_Grises():
    try:
        __ruta_Img_Original = objImagen.getImg_Original()
        if __ruta_Img_Original != "":
            image_64_encode = objImagen.Escala_Grises(__ruta_Img_Original)
        else:
            image_64_encode =""
        return {"img_escala_grises" : image_64_encode}
    except Exception as e:
            print(str(e))


