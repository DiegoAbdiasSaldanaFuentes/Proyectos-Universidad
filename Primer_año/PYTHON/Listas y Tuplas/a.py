def lee_datos():
    tablero = ['DOFGO','BARCO', 'OLUZA','TCTIA']
    palabras =['AZUL','ZULO','ARCO','RUTA','DRAGON']
    return tablero, palabras

def izq_der (tablero,palabra):
    for linea in tablero:
        if palabra in linea:
            return 'SI'
    return 'NO'

def der_izq(tablero,palabra):
    for linea in tablero:
        cadena = ''
        for letra in linea:
            cadena = letra + cadena
        if palabra in cadena:
            return 'SI'
    return 'NO'
        
def proceso (tablero, palabras):
    solucion = []
    for palabra in palabras:
        esta1 = izq_der(tablero, palabra)
        esta2 = der_izq(tablero, palabra)
        if esta1 == 'SI' or esta2 == 'SI':
            solucion.append([palabra +'- Si'])
        else:
            solucion.append([palabra + '- No'])
    return solucion

def genera_solucion(solucion):
    print(solucion)

if __name__ == "__main__":
    tablero, palabras = lee_datos()
    solucion = proceso(tablero, palabras)
    genera_solucion(solucion)