def lectura_datos(archivo):
    ent = open(archivo)
    i = []
    for linea in ent:
        linea =linea.rstrip("\n")
        lista = linea.split(',')
        i.append(lista)
    ent.close()
    return i

def funcion_a(i):
    aves = []
    for ave in i:
        login = ave[7] + ave[2]
        aves.append(login)
    
    return aves

      




if __name__ == "__main__":
    pajaros = lectura_datos("aves.txt")
    pajaros_regiones = funcion_a (pajaros)
   

print(pajaros_regiones)
