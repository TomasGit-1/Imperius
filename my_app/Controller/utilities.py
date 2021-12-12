import json
import os
import random
import string



def cargaConfig():
    configuration = None
    try:
        with open(os.getcwd()+"/Config/configAPI.json", "r" , encoding="utf-8") as f:
            configuration = json.loads(f.read())
            return configuration
    except  Exception as e:
        print(e)

def readAlgoritmo(path):
    code=[]
    with open(path, 'r') as f:
        lineas = f.readlines()

    for line in lineas:
        code.append(line)
    
    return code
        


def GuardarAlgoritmo(path , data ):
    with open(path, 'w') as f:
        for item in data:
            f.write(item)

    return True


def nameRandom(number_of_strings):
    number_of_strings = 5
    length_of_string = 8
    cadena = ""
    for x in range(number_of_strings):
        cadena = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
    return cadena

def CrearRegistro(rutafile,registro , operador ):
    if not os.path.exists(rutafile):
        os.mkdir(rutafile)
    archivo = rutafile+"operadores"+".txt"

    #Se agrega nombre del operador 
    fs = open(archivo, 'a')
    fs.write("operador:"+operador+"{")
    fs.write("\n")
    fs.close()

    with open(archivo, "a") as archivoCreate:
        for i in registro:
            for key , item in i.items():
                archivoCreate.write("\t %s %s" %(key , item))
                archivoCreate.write("\n")
        archivoCreate.write("}")
        archivoCreate.write("\n")

    return archivo

def ReadRegistro(archivo):
    with open(archivo, "r") as archivoRead:
        lineas = archivoRead.readlines()

    listaFinal , listaTemp = [] , []
    diccionario = []
    for i in lineas:
        if "}" in i :
            #Codigo para filtrar los peradores del txt
            diccionario = []
            for y in listaTemp:
                y = y.strip()
                resultado = y.find(":")
                diccionario.append( [y[:resultado] ,y[resultado+1:]])
            listaFinal.append(diccionario)
            listaTemp.clear()
        else: 
            listaTemp.append(i)

    return listaFinal

def getOperator(ruta):
    file = []
    with open(ruta , "r") as lines:
        file = lines.readlines()
    return file

def RescribirOperator(ruta , lista):
    file = []
    with open(ruta , "w") as lines:
        for i in lista:
            file = lines.write(i)
