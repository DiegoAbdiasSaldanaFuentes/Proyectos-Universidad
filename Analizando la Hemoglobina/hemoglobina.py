
edad= 12
nivel_hemoglobina= 16
escala_edad="1"
genero="1"



if escala_edad == "0":
        if  edad <= 1:
            minimo,maximo= 13, 26
        elif edad <= 6:
            minimo,maximo= 10,18
        elif edad <= 12:
            minimo,maximo=11,15
if  escala_edad == "1":
        if edad <= 5:
            minimo,maximo= 11.5, 15
        elif edad <=10:
            minimo,maximo= 12.6, 15.5
        elif edad <=15:
            minimo,maximo= 13,15.5
#hombre
if genero == "0" and escala_edad== 1:
        if edad > 15:
            minimo,maximo= 12,16
#mujer
if genero == "1" and escala_edad ==1:
        if edad > 15:
            minimo,maximo= 14 ,18 


if nivel_hemoglobina <= minimo:
    print ("negativo")
elif nivel_hemoglobina >= maximo:
    print  ("positivo")
else:
    print ("dentro del rango")


