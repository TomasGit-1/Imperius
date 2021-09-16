from flask import Blueprint , render_template , request
import os
from Controller.utilities import cargaConfig , nameRandom , CrearRegistro
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
            #Obtenemos los datos de la interfaz
            file = request.files['file']
            var_Original = request.values['identificador']
            __ruta_Img_Original = os.getcwd() + configuration["general"][0]["Imagenes"]
            
            #Creamos la carpeta para las imagenes
            if not os.path.exists(__ruta_Img_Original):
                os.mkdir(__ruta_Img_Original)
            __ruta_Img_Original = __ruta_Img_Original + id + file.filename
            file.save(__ruta_Img_Original)

            #Enviamos los datos al clase para guardarlos
            objImagen.setImg_ruta(__ruta_Img_Original)
            objImagen.setIdentificador(var_Original)
            objImagen.setMetodo("cargar_image")

            #Generamos la imagen en base64 para retornarla y pintar
            image_64_encode = objImagen.Base64(__ruta_Img_Original)

            #Obtenemos el registros de los operadoresTxt
            registro = objImagen.getModelo()
            CrearRegistro(os.getcwd() + configuration["general"][0]["OperadoresTxt"], registro , "cargar_image")
            return {"img_Orginal" : image_64_encode ,"registro" : registro}
        except FileNotFoundError:
            return "Folder no existe"
        except Exception as e:
            print(str(e))

@api_Imperius.route("/escala_grises" , methods = ['POST'])
def Escala_Grises():
    try:
        __ruta_Img_Original = objImagen.getImg_ruta()
        var_EscalaGrises = ""
        if request.method == "POST":
            var_EscalaGrises = request.values['identificador']

        if __ruta_Img_Original != "":
            image_64_encode , ruta_escala_grises = objImagen.Escala_Grises(__ruta_Img_Original)
            #Enviamos los datos al clase para guardarlos
            objImagen.setImg_ruta(ruta_escala_grises)
            objImagen.setIdentificador(var_EscalaGrises)
            objImagen.setMetodo("Escala_Grises")
            registro = objImagen.getModelo()
            CrearRegistro(os.getcwd() + configuration["general"][0]["OperadoresTxt"], registro , "escala_grises")
        else:
            image_64_encode =""
        
        registro = ""
        return {"img_escala_grises" : image_64_encode , "registro" : registro}
    except Exception as e:
            print(str(e))


