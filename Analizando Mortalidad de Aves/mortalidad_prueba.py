#CODIGO SIN TERMINAR
import re
import matplotlib.pyplot as plt
def lectura_datos (archivo):
    ent = open(archivo)
    datos=[]
    for linea in ent:
        linea= linea.rstrip("\n")
        linea = linea.lower()
        partes = re.split("[-,]",linea)
        datos.append(partes)
    ent.close
    return datos

def funcion_a (datos):
    


if __name__ =="__main__":
    lectura = lectura_datos("aves.txt")
    aves_region = funcion_a(lectura)

print(lectura)
