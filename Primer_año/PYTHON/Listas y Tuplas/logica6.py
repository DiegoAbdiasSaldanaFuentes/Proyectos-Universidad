def lee_raw(nombre):
    ent = open(nombre)
    crudo = []
    for linea in ent:
        linea = linea.rstrip("/n")
        crudo.append(linea)
    ent.close()

def cambia(crudo):  # Define la función que recibe 'crudo' (una lista de líneas).
    datos = []  # Crea una lista vacía 'datos' para almacenar las líneas modificadas.
    for linea in crudo:  # Recorre cada línea en la lista 'crudo'.
        salida = ''  # Crea una cadena vacía 'salida' que será la línea modificada.
        i = 0  # Empieza en el índice 0 para recorrer la línea carácter por carácter.
        while i < len(linea):  # Mientras no llegue al final de la línea...
            caracter = linea[i]  # Toma el carácter en la posición 'i'.
            if caracter == '"':  # Si encuentra una comilla...
                salida = salida + caracter  # Añade la comilla a 'salida'.
                i = i + 1  # Pasa al siguiente carácter.
                caracter = linea[i]  # Toma el siguiente carácter.
                while caracter != '"':  # Mientras no encuentre otra comilla...
                    if caracter == ',':  # Si el carácter es una coma...
                        caracter = ';'  # Cambia la coma por un punto y coma.
                    salida = salida + caracter  # Añade el carácter modificado o no a 'salida'.
                    i += 1  # Avanza al siguiente carácter.
                salida = salida + '"'  # Cuando encuentra la segunda comilla, la añade.
            else:
                salida = salida + caracter  # Si no hay comillas, añade el carácter tal cual.
            i = i + 1  # Avanza al siguiente carácter.
        salida = salida.rstrip(',')  # Elimina comas al final de la línea.
        datos.append(salida)  # Añade la línea modificada a 'datos'.
    return datos  # Devuelve la lista 'datos' con las líneas modificadas.

    
def nuevo(datos):
    for dato in datos:
        print(dato)  # Imprimimos cada línea de datos correctamente

if __name__ == '__main__':
    crudo = ['1,"Perez, Sra. Juana Soto",Femenino,29,0,0,24160"Talca, Maule"']
    datos = cambia(crudo)
    nuevo(datos)
