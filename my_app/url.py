from flask import Blueprint , render_template , request
import os
from Controller.utilities import cargaConfig , nameRandom , CrearRegistro , ReadRegistro
from Api.Imagen import Imagen


api_Imperius = Blueprint('api_Imperius' , __name__)
configuration = cargaConfig()
ruta_Img_Original = ""
objImagen = Imagen()
registro = []


@api_Imperius.route("/")
def home():
    return render_template("home.html")

@api_Imperius.route("/imperius/")
def Home_App():
    return render_template("imperius.html")

@api_Imperius.route("/cargar_image", methods = ['POST'])
def cargar_image():
    ruta_Img_Original = ""
    id = nameRandom(5)
    if request.method == "POST":
        try:

            #Obtenemos los datos de la interfaz
            file = request.files['file']
            var_Original = request.values['identificador']
            ruta_Img_Original = os.getcwd() + configuration["general"][0]["Imagenes"]
            
            #Creamos la carpeta para las imagenes
            if not os.path.exists(ruta_Img_Original):
                os.mkdir(ruta_Img_Original)
            ruta_Img_Original = ruta_Img_Original + id + file.filename
            file.save(ruta_Img_Original)
            
            #Enviamos los datos al clase para guardarlos
            #ruta , identificador , modelo
            objImagen.setDatos([ruta_Img_Original , var_Original , "cargar_image"])
            objImagen.setImg_ruta(ruta_Img_Original)
            
            #Generamos la imagen en base64 para retornarla y pintar
            image_64_encode = objImagen.Base64(ruta_Img_Original)
            #Obtenemos el modelo que vamos a mostar en la tabla
            datos = objImagen.getModelo()
            
            #Obtenemos el registros de los operadoresTxt
            registro = objImagen.getModeloFinal(datos)
            
            return {"img_Orginal" : image_64_encode ,"registro" : registro }
        except FileNotFoundError:
            return "Folder no existe"
        except Exception as e:
            print(str(e))

@api_Imperius.route("/escala_grises" , methods = ['POST'])
def Escala_Grises():
    try:
        ruta_Img_Original = objImagen.getImg_ruta()
        var_EscalaGrises = ""
        if request.method == "POST":
            var_EscalaGrises = request.values['identificador']

        if ruta_Img_Original != "":
            image_64_encode , ruta_escala_grises = objImagen.Escala_Grises(ruta_Img_Original)
            objImagen.LimpiarMemoria()
            #Enviamos los datos al clase para guardarlos
            objImagen.setDatos([ruta_escala_grises , var_EscalaGrises , "Escala_Grises"])
            #Obtenemos el modelo que vamos a mostar en la tabla
            datos = objImagen.getModelo()

            registro = objImagen.getModeloFinal(datos)
            return {"img_escala_grises" : image_64_encode , "registro" : registro}
        else:
            image_64_encode =""
            registro = []            
            return {"img_escala_grises" : image_64_encode , "registro" : registro}
    except Exception as e:
        print(str(e))


@api_Imperius.route("/limpiar_memoria" , methods = ['POST'])
def Limpiar_Memoria():
    try:
        registro = []
        objImagen.LimpiarMemoria()
        objImagen.LimpiarModelo()
        return { "registro" : registro}
    except Exception as e:
        print(str(e))

@api_Imperius.route("/eliminar_operador" , methods = ['POST'])
def Eliminar_Operador():
    if request.method == 'POST':
        posicion = int(request.values['posicion'])
    registro = objImagen.Eliminar(posicion)

    return { "registro" : registro}

