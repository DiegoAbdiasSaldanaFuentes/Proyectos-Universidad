

#importamos el matplotlib para poder hacer  un grafico de barras
import matplotlib.pyplot as plt




# al crear el for haremos que la funcion "linea" sea modife a si mismo para que haga un salto de linea al acabar la linea justo con split para separar los datos en las comas.
def lectura_datos(archivo):
    ent = open(archivo) 
    Datos = []
    for linea in ent:
        linea =linea.rstrip("\n")
        lista = linea.split(',')
        Datos.append(lista)
    ent.close()
    return Datos



#La funcion(a) indica las muertes totales por region.
def funcion_a(Datos):
    aves_por_region = {}
    for aves_muertes_region in Datos:
        region = aves_muertes_region [3]
        muertes = int(aves_muertes_region[7])
        if region not in aves_por_region:
            aves_por_region[region] = 0
        aves_por_region[region] = aves_por_region[region] + muertes
    return aves_por_region


#La funcion(b) indica la cantidad de aves muertas para el mes de enero y el año 2023.
def funcion_b(Datos):
    muertes_enero_2023 = 0
    for muer_ener in Datos:
        fecha = muer_ener[0]
        mes  = fecha.split('-')[1]
        año = fecha.split('-')[2]
        if mes == '01' and año == '2023':
            muertes_enero_2023 = muertes_enero_2023 + int(muer_ener[7])
    return muertes_enero_2023


#La funcion(c) indica la cantidad de muertes de la especie Tagua en la comuna de Cartagena.

def funcion_c(Datos):
    muertes_tagua_cartagena = 0
    for taguacar in Datos:
        comuna = taguacar[3]
        especie = taguacar[6]
        if comuna == 'Cartagena' and especie == 'Tagua - (Fulica armillata)':
            muertes_tagua_cartagena = muertes_tagua_cartagena + int(taguacar[7])
    return muertes_tagua_cartagena


#La funcion(d) busca el numero de muertes de la especie Piquero en una fecha especifica(12/02/2023).
def funcion_d(Datos):
    muertes_piquero_12_feb_2023 = 0
    for pique_12 in Datos:
        fecha = pique_12[0]
        especie =pique_12[6]
        if fecha == '12-02-2023' and especie == 'Piquero - (Sula variegata)':
            muertes_piquero_12_feb_2023 =  muertes_piquero_12_feb_2023 +  int(pique_12[7])
    return muertes_piquero_12_feb_2023

#La funcion(d2) busca el numero de muertes de la especie Gaviota garuma en una fecha especifica(12/02/2023).

def funcion_d2(Datos):
    muertes_gaviota_12_feb_2023 = 0
    for gaviota_12 in Datos:
        fecha = gaviota_12[0]
        especie = gaviota_12[6]
        if fecha == '12-02-2023' and especie == 'Gaviota garuma - (Larus modestus)':
            muertes_gaviota_12_feb_2023 =  muertes_piquero_12_feb_2023 +  int(gaviota_12[7])
    return muertes_gaviota_12_feb_2023


# creamos una nueva variable donde estara la lista de las especies que necesitaremos graficar
def funcion_e(Datos):
    especies_interes = ['Gaviota garuma - (Larus modestus)', 'Piquero - (Sula variegata)', 'Gaviota de Franklin - (Larus pipixcan)', 'Pelicano - (Pelecanus thagus)', 'Guanay - (Phalacrocorax bougainvillii)']
    muertes_por_especie = {especie: 0 for especie in especies_interes}
    for especie_graf in Datos:
        especie = especie_graf[6]
        if especie in muertes_por_especie:
            muertes_por_especie[especie] +=  muertes_por_especie  and int(especie_graf[7])
    return muertes_por_especie


#para crear el grafico usaremos el ".bar" para que uselos datos de las muertes y nombre de especies luego le pondremos nombre a la grafica
def grafica(grafico):
    plt.figure(figsize=(15,4))
    plt.bar(grafico.keys(), grafico.values())
    plt.xlabel('Especies')
    plt.ylabel('Número de muertes')
    plt.title('Muertes de aves por especie')
    plt.show()


#creamos la salida de todas nuestras funciones
def genera_salida(pajaros_regiones, muertes_enero_2023, muertes_tagua_cartagena, muertes_gaviota_12_feb_2023):
    sal = open('resultado.txt', 'w')
    sal.write('Autores: Victor Farias - Diego Saldana'+'\n\n')
    sal.write('cantidad de aves muertas por region:'+'\n\n')
    for aves_reg in pajaros_regiones:
        muertes = pajaros_regiones[aves_reg]
        sal.write('  '' Region: ' + aves_reg + ', Muertes: ' + str(muertes) + '\n\n')
    
    sal.write('Casos aves muertas mes de enero del ano 2023: '+ str(muertes_enero_2023)+'\n\n')
    sal.write('En la comuna de Cartagena se detectaron '+str(muertes_tagua_cartagena)+' Taguas muertas'+'\n\n')
    sal.write('Las muertes detectadas para el 12 de febrero del 2023 de la especie Gaviota garuma son: '+str(muertes_gaviota_12_feb_2023)+'\n\n')
    sal.close()
   
   



# creamos la guia de todas nuestras funciones

if __name__ == "__main__":
    pajaros = lectura_datos("aves.txt")
    pajaros_regiones = funcion_a (pajaros)
    muertes_enero_2023 = funcion_b (pajaros)
    muertes_tagua_cartagena = funcion_c (pajaros)
    muertes_piquero_12_feb_2023 = funcion_d (pajaros)
    muertes_gaviota_12_feb_2023 = funcion_d2 (pajaros)
    especies_muertas = funcion_e (pajaros)
    grafica(especies_muertas)
    genera_salida(pajaros_regiones, muertes_enero_2023, muertes_tagua_cartagena, muertes_gaviota_12_feb_2023)
    
# Generamos la salida
print()