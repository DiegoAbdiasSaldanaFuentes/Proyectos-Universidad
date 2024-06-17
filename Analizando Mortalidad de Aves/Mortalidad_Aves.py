import matplotlib.pyplot as plt




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
    aves_por_region = {}
    for avereg in i:
        region = avereg[3]
        muertes = int(avereg[7])
        if region not in aves_por_region:
            aves_por_region[region] = 0
        aves_por_region[region] = aves_por_region[region] + muertes
    return aves_por_region


def funcion_b(i):
    muertes_enero_2023 = 0
    for muer_ener in i:
        fecha = muer_ener[0]
        mes, año = fecha.split('-')[1], fecha.split('-')[2]
        if mes == '01' and año == '2023':
            muertes_enero_2023 = muertes_enero_2023 + int(muer_ener[7])
    return muertes_enero_2023

# comuna esta en 3 y pajaro en 6
def funcion_c(i):
    muertes_tagua_cartagena = 0
    for taguacar in i:
        comuna = taguacar[3]
        especie = taguacar[6]
        if comuna == 'Cartagena' and especie == 'Tagua':
            muertes_tagua_cartagena = muertes_tagua_cartagena + int(taguacar[7])
    return muertes_tagua_cartagena
      

def funcion_d(i):
    muertes_piquero_12_feb_2023 = 0
    for pique_12 in i:
        fecha = pique_12[0]
        especie =pique_12[6]
        if fecha == '12-02-2023' and especie == 'Piquero':
            muertes_piquero_12_feb_2023 =  muertes_piquero_12_feb_2023 +  int(pique_12[7])
    return muertes_piquero_12_feb_2023



def funcion_e(i):
    especies_interes = ['Gaviota garuma', 'Piquero', 'Gaviota de Franklin', 'Pelicano', 'Guanay']
    muertes_por_especie = {especie: 0 for especie in especies_interes}
    for especie_graf in i:
        especie = especie_graf[6]
        if especie in muertes_por_especie:
            muertes_por_especie[especie] =  muertes_por_especie + int(especie_graf[7])
    return muertes_por_especie

if __name__ == "__main__":
    pajaros = lectura_datos("aves.txt")
    pajaros_regiones = funcion_a (pajaros)
    muertes_enero_2023 = funcion_b (pajaros)
    muertes_tagua_cartagena = funcion_c (pajaros)
    muertes_piquero_12_feb_2023 = funcion_d (pajaros)
    grafico = funcion_e (pajaros)



    

print(grafico)