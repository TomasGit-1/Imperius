#Desarrollado por : Tomas Lopez Perez
#Año de creacion 2021
from flask import Blueprint , render_template , request
import os
from Controller.utilities import cargaConfig , nameRandom , getOperator
from Api.Imagen import Imagen
import ast


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

@api_Imperius.route("/operators", methods = ['POST'])
def operators():
    if request.method == 'POST':
        try:
            route_file = os.getcwd() + configuration["general"][0]["OperadoresTxt"]
            operator = getOperator(route_file)
            return {"operator" : operator}
        except FileNotFoundError:
            return "Folder no existe"
        except Exception as e:
            print(str(e))

@api_Imperius.route("/cargar_image", methods = ['POST'])
def cargar_image():
    ruta_Img_Original = ""
    id = nameRandom(5)
    if request.method == "POST":
        try:
            #Obtenemos los datos de la interfaz
            file = request.files['file']
            operador = request.values['operador']
            data = request.values['data']
            data = data.split(',')
            identificador =data[1]
            ruta_Img_Original = os.getcwd() + configuration["general"][0]["Imagenes"]

            #Creamos la carpeta para las imagenes
            #Se crea primero la carpeta Image si no esta creada 
            if not os.path.exists(ruta_Img_Original):
                os.mkdir(ruta_Img_Original)
            #Despues se genera la ruta de la imagen
            ruta_Img_Original = ruta_Img_Original + id  + file.filename
            #Guardamos la imagen
            file.save(ruta_Img_Original)
            
            #Enviamos los datos al clase para guardarlos
            #ruta , identificador , operador
            objImagen.setDatos([ruta_Img_Original , identificador , operador])
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

@api_Imperius.route("/Api/Operadores" , methods = ['POST'])
def operadores():
    #Obtenemos los datos de la interfaz
    #Obtenemos los datos de la interfaz
    file = request.files['file']
    operador = request.values['operador']
    data = request.values['data']
    data = data.split(',')
    identificador =data[0]
    image_64_encode = 0
    escala_grises = 0
    try:
        #comando = 'image_64_encode , escala_grises = objImagen.'+operador+'(rutaOriginal)'
        exec('objImagen.'+operador+'(data)')
    except Exception as e:
        print(str(e))
    objImagen.LimpiarMemoria()
    image_64_encode , escala_grises = objImagen.getEncodeImg()
    #Enviamos los datos al clase para guardarlos
    objImagen.setDatos([escala_grises , identificador, operador])
    # objImagen.setImg_ruta(ruta_Img_Original)
            
    # #Generamos la imagen en base64 para retornarla y pintar
    # image_64_encode = objImagen.Base64(ruta_Img_Original)
    #Obtenemos el modelo que vamos a mostar en la tabla
    datos = objImagen.getModelo()


    registro = objImagen.getModeloFinal(datos)
    return {"img_Orginal" : image_64_encode , "registro" : registro}

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




#Podria servir No borrar por el momento
#Muchas horas de trabajo

# @api_Imperius.route("/escala_grises" , methods = ['POST'])
# def Escala_Grises():
#     try:
#         ruta_Img_Original = objImagen.getImg_ruta()
#         var_EscalaGrises = ""
#         if request.method == "POST":
#             var_EscalaGrises = request.values['identificador']

#         if ruta_Img_Original != "":
#             image_64_encode , ruta_escala_grises = objImagen.Escala_Grises(ruta_Img_Original)
#             objImagen.LimpiarMemoria()
#             #Enviamos los datos al clase para guardarlos
#             objImagen.setDatos([ruta_escala_grises , var_EscalaGrises , "escala_grises"])
#             #Obtenemos el modelo que vamos a mostar en la tabla
#             datos = objImagen.getModelo()

#             registro = objImagen.getModeloFinal(datos)
#             return {"imagen" : image_64_encode , "registro" : registro}
#         else:
#             image_64_encode =""
#             registro = []            
#             return {"imagen" : image_64_encode , "registro" : registro}
#     except Exception as e:
#         print(str(e))

# @api_Imperius.route("/detectar_bordes" , methods = ['POST'])
# def Detectar_Bordes():
#     try:
#         ruta_Img_Original = objImagen.getImg_ruta()
#         idImg = ""
#         if request.method == "POST":
#             idImg = request.values['identificador']

#         if ruta_Img_Original != "":
#             image_64_encode , ruta_imag = objImagen.detectar_bordes(ruta_Img_Original)
#             objImagen.LimpiarMemoria()
#             #Enviamos los datos al clase para guardarlos
#             objImagen.setDatos([ruta_imag , idImg , "detectar_bordes"])
#             #Obtenemos el modelo que vamos a mostar en la tabla
#             datos = objImagen.getModelo()

#             registro = objImagen.getModeloFinal(datos)
#             return {"imagen" : image_64_encode , "registro" : registro}
#         else:
#             image_64_encode =""
#             registro = []            
#             return {"imagen" : image_64_encode , "registro" : registro}
#     except Exception as e:
#         print(str(e))

# @api_Imperius.route("/blur" , methods = ['POST'])
# def blur_Image():
#     try:
#         ruta_Img_Original = objImagen.getImg_ruta()
#         idImg = ""
#         if request.method == "POST":
#             idImg = request.values['identificador']

#         if ruta_Img_Original != "":
#             image_64_encode , ruta_imag = objImagen.blur_imagen(ruta_Img_Original)
#             objImagen.LimpiarMemoria()
#             #Enviamos los datos al clase para guardarlos
#             objImagen.setDatos([ruta_imag , idImg , "blur_imagen"])
#             #Obtenemos el modelo que vamos a mostar en la tabla
#             datos = objImagen.getModelo()

#             registro = objImagen.getModeloFinal(datos)
#             return {"imagen" : image_64_encode , "registro" : registro}
#         else:
#             image_64_encode =""
#             registro = []            
#             return {"imagen" : image_64_encode , "registro" : registro}
#     except Exception as e:
#         print(str(e))


# @api_Imperius.route("/rota_img" , methods = ['POST'])
# def rota_img():
#     try:
#         ruta_Img_Original = objImagen.getImg_ruta()
#         idImg = ""
#         if request.method == "POST":
#             idImg = request.values['identificador']
#         if ruta_Img_Original != "":
#             image_64_encode , ruta_imag = objImagen.rotar_imagen(ruta_Img_Original)
#             objImagen.LimpiarMemoria()
#             #Enviamos los datos al clase para guardarlos
#             objImagen.setDatos([ruta_imag , idImg , "rotar_imagen"])
#             #Obtenemos el modelo que vamos a mostar en la tabla
#             datos = objImagen.getModelo()

#             registro = objImagen.getModeloFinal(datos)
#             return {"imagen" : image_64_encode , "registro" : registro}
#         else:
#             image_64_encode =""
#             registro = []            
#             return {"imagen" : image_64_encode , "registro" : registro}
#     except Exception as e:
#         print(str(e))



# @api_Imperius.route("/FiltrosGr" , methods=["POST"])
# def FiltrosGr(): 
#     try:
#         ruta_Img_Original = objImagen.getImg_ruta()
#         idImg = ""   
#         if request.method == "POST":
#             idImg = request.values['data']
#             data=idImg.split(',')
#             idImg =data[0]

#         if ruta_Img_Original != "":
#             image_64_encode , ruta_imag = objImagen.FiltrosClassGR(data[2:] , data[1])

#         objImagen.LimpiarMemoria()
#         #Enviamos los datos al clase para guardarlos
#         objImagen.setDatos([ruta_imag , idImg , "rotar_imagen"])
#         #Obtenemos el modelo que vamos a mostar en la tabla
#         datos = objImagen.getModelo()

#         registro = objImagen.getModeloFinal(datos)
#         return {"imagen" : image_64_encode , "registro" : registro}

#     except Exception as e:
#         print(str(e))






