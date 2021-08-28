import json
import os
import random
import string



def cargaConfig():
    configuration = None
    try:
        with open(os.getcwd() +"/my_app/Config/configAPI.json", "r" , encoding="utf-8") as f:
            configuration = json.loads(f.read())
            return configuration
    except  Exception as e:
        print(e)

def nameRandom(number_of_strings):
    number_of_strings = 5
    length_of_string = 8
    cadena = ""
    for x in range(number_of_strings):
        cadena = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
    return cadena
