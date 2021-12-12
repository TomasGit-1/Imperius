class Imagen():
    valor = [1, 2, 3, 4 ]
    def __init__(self):
        print ("Entramos a la clase Imagen")

    def msg(self):
        print("Este es un mensaje en python"+str(self.valor))

    def msg(self):
        print("Este es un mensaje en python"+str(self.valor))

def msg1(params):
        print("Hola Mundo mi nombre es "+str(params))

# img = Imagen()
# x = getattr(img, 'msg')

locals()['msg1']("Tomas 0")
globals()['msg1']("Tomas 1")


exec('print("--------------------------------------------")')
img = Imagen()
#exec('img = Imagen()')
exec('img.msg()')


