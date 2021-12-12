# Imperius
    Este proyecto es para entregar las practicas profesionales

# Para correr la pagina web siga los siguientes pasos
    1.- Instalar version de python 3.8
        https://www.python.org/downloads/

    2.- Instalacion y creacion de entorno virtual 
        pip install virtualenv
        Entrar a  una carpeta donde estara el proyecto
        Ejemplo /home/metrics/Documentos/Personal/ProyectosUabjo/Imperius

        Dentro de la carpte a correr el comando virtualenv ImperiusEnv
        dentro del entorno creado ejecutar el comando 
        git clone https://github.com/TomasGit-1/Imperius.git

        Dentro del repositorio clonarlo crear un segundo entorno dentro del primer entorno activado
        

    3.- Es recomendable utilizar el Editor de text VsCode

    4.- Para instalar las librerias ejecute el siguiente comando dentro de la carpeta my_app/resources

        pip install -r requeriments.txt 
        
# Documentacion de librerias utilizadas para el procesamiento de las imagenes
    https://pillow.readthedocs.io/en/stable/
    https://docs.opencv.org/4.5.3/d4/d86/group__imgproc__filter.html

# Documentacion del proyecto + calendario de actitvidades
    https://docs.google.com/document/d/1A7PNkn4WV8ijNWrlu-3EsSrAD8T6hqtw/edit?usp=sharing&ouid=117800488039180460578&rtpof=true&sd=true


# Para se tiene problemas al comparar el String del txt con el codigo
    if(array[i+1] == 'input'){
        console.log('Entro a la condicion 1 ')
        $(wrapper).append('<div id="content"> <h4 style="display:inline;">'+i+' </h4>  <input type='+array[i+1]+' name="mytext[]" style ="display:inline;"/> <br> </div>');
    }
    Se decide apllicar un id a cada compontente 
    0 == input
    1 == select o b-form-select

# Para el algoritmo
    Cada instruccion debe ser separada por ;
    #Ejemplo
        data = ["identificador" , 15 , 17];
        d = int(data[1]);