# Autor: Hugo Araya Carrasco
# Fecha: 07/08/2024
# Version : 0.0

def lectura(nombre):
    ent = open(nombre)
    linea1 = ent.readline().rstrip('\n')
    linea2 = ent.readline().rstrip('\n')
    return linea1, linea2


if __name__ == '__main__':
    coaliciones, votacion = lectura('votos.txt')
   


