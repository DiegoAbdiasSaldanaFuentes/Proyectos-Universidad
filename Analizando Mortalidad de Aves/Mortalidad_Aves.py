

#importamos el matplotlib para poder hacer  un grafico de barras
import matplotlib.pyplot as plt



# creamos  un Def para crear una función a la que llamaremos "lectura_datos" y creamos una variable llamada "archivo" que recibira informacion de la función.
# tambien creamos la entrada o ent donde abrira el archivo que lo abre lectura_datos que abre "aves.txt" para poder abrir el texto.
# seguimos con los Datos para crear la lista para  crear un for con una funcion llamada linea porque  for  ira line por linea en "ent".
# al crear el for haremos que la funcion "linea" sea modife a si mismo para que haga un salto de linea al acabar la linea justo con split para separar los datos en las comas.
# despues cerramos el archivo para evitar cualquier tipo de perdida de informacion.

def lectura_datos(archivo):
    ent = open(archivo) 
    Datos = []
    for linea in ent:
        linea =linea.rstrip("\n")
        lista = linea.split(',')
        Datos.append(lista)
    ent.close()
    return Datos


# creamos un Def para la "funcion_a"
# creamos la variable "aves_por_region" con cadenas  para evitar elementos repetidos o que la funcion tire error
# creamos un for para la funcion "aves_por_region" que estara buscando en "Datos"
# Luego creamo variables llamadas "region" y "muertes"   que son los elemntos que estan  en las posiciones [3] y [7] con la excepcion de que la posicion [7] le agregamos un Int al principio para que la funcion reconozca que la posicion [7] es un numero y no un string
# creamos un if para poder decir que si hay una "region"  en "aves_por_region" que ya este osea se repite se sume si no es el caso no se suma osea se mantiene en 0, lo mismo pasa con las muertes con la excepcion de que debe sumarse todo
# retornamos la funcion para que nos muestre el resutado

def funcion_a(Datos):
    aves_por_region = {}
    for aves_muertes_region in Datos:
        region = aves_muertes_region [3]
        muertes = int(aves_muertes_region[7])
        if region not in aves_por_region:
            aves_por_region[region] = 0
        aves_por_region[region] = aves_por_region[region] + muertes
    return aves_por_region

# creamos un Def para la "funcion_b"
# hacemos un contador que comienze en 0 
# creamos un for con la funcion llamada "muer_ener" osea muertes_enero simplificado, que busque en datos la fecha del mes y año
# especificamos en donde  esta la posicion del mes y el año
# creamos  un if  para decir si mes es igual a "01" y año es igual a "2023" para que busque en esas fechas si es asi muertes_enero2023 se sumara consigo mismo para sumar sus respectivas muertes
# devolvemos la funcion para que nos muestre el resultado

def funcion_b(Datos):
    muertes_enero_2023 = 0
    for muer_ener in Datos:
        fecha = muer_ener[0]
        mes  = fecha.split('-')[1]
        año = fecha.split('-')[2]
        if mes == '01' and año == '2023':
            muertes_enero_2023 = muertes_enero_2023 + int(muer_ener[7])
    return muertes_enero_2023


# creamos un def para la "funcion_c"
# hacemos un contador que empieze en 0
# creamos un for con la funcion llamada "taguacar" que simplifica tagua y cartagena
# creamos una variable llamada "comuna" y "especie" detallando las pocisiones en las que  se encuentra
# creamos un if que sume Cartagena si encuentra otro Cartagena, lo mismo aplica con Tagua y cuando lo haga que sume las muertes
# al final que nos devuelva "Muertes_Tagua_Cartagena"

def funcion_c(Datos):
    muertes_tagua_cartagena = 0
    for taguacar in Datos:
        comuna = taguacar[3]
        especie = taguacar[6]
        if comuna == 'Cartagena' and especie == 'Tagua - (Fulica armillata)':
            muertes_tagua_cartagena = muertes_tagua_cartagena + int(taguacar[7])
    return muertes_tagua_cartagena


# creamos un def  con la "funcion_d"
# creamos un contador que empieze en 0 
# creamos un for con la funcion llamada "pique_12" simplificando piquero y 12 de febrero
# creamos variables llamadas fecha y especie con sus respectivas posiciones
# creamos un if con las variablles fechas y especias las cuales deben ser iguales a la fecha entregada y a la especie osea piquero y cuando lo haga sume las muertes
# finalmente retornamos "muertes_piquero_12_feb_2023"

def funcion_d(Datos):
    muertes_piquero_12_feb_2023 = 0
    for pique_12 in Datos:
        fecha = pique_12[0]
        especie =pique_12[6]
        if fecha == '12-02-2023' and especie == 'Piquero - (Sula variegata)':
            muertes_piquero_12_feb_2023 =  muertes_piquero_12_feb_2023 +  int(pique_12[7])
    return muertes_piquero_12_feb_2023


# creamos el Def para si poder tener la "funcion_e"
# creamos una nueva variable donde estara la lista de las especies que necesitaremos graficar
# usaremos esta vez un diccionario donde sera ma s facil mostrar las muertes de las especies mencionada 
# creamos un for con la funcion "especie_graf" que buscara en "Datos"
# hacemos una variable "especie" que nos diga que las especies de aves.txt se encuentra en la posicion [6]
# hacemos un if  donde usaremos la variable ya creada "especie" que use el diccionario "muertes_po_especie" que si "muertes_por_especie" en la variable especie es igual a esta miesma  se sume  y usando "and" sumaremos las muertes
# finalmente retornamos "muertes_por_especie"

def funcion_e(Datos):
    especies_interes = ['Gaviota garuma - (Larus modestus)', 'Piquero - (Sula variegata)', 'Gaviota de Franklin - (Larus pipixcan)', 'Pelicano - (Pelecanus thagus)', 'Guanay - (Phalacrocorax bougainvillii)']
    muertes_por_especie = {especie: 0 for especie in especies_interes}
    for especie_graf in Datos:
        especie = especie_graf[6]
        if especie in muertes_por_especie:
            muertes_por_especie[especie] +=  muertes_por_especie  and int(especie_graf[7])
    return muertes_por_especie






# creamos la guia de todas nuestras funciones

if __name__ == "__main__":
    pajaros = lectura_datos("aves.txt")
    pajaros_regiones = funcion_a (pajaros)
    muertes_enero_2023 = funcion_b (pajaros)
    muertes_tagua_cartagena = funcion_c (pajaros)
    muertes_piquero_12_feb_2023 = funcion_d (pajaros)
    grafico = funcion_e (pajaros)
    
# printiamos la salida
print(pajaros)