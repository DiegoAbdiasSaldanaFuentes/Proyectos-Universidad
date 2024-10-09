def lee_dimension (ar):
    dimension = ar.readline().rstrip('\n').split('')
    dimension[0] = int(dimension[0])
    dimension[1] = int(dimension[1])
    return dimension

def lee_centro(ar):
    centro =ar.readline().rstrip('\n').split('')
    centro[0] = int(centro[0])
    centro[1] = int(centro[1])
    return centro

def  str_a_int (linea):
    i = 0
    while i < len(linea):
        linea[i] = int(linea[i])
        i = i + 1
    return linea

def lee_tablero(ar,filas):
    tablero = []