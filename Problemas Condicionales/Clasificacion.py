#un programa para clasificar edades

edad= int(input("ingrese la edad que desea clasificar:")) 

if edad <= 2:
    print("es un bebé")
elif edad <= 12:
    print("es un niño")
elif edad <=17:
    print("es un adolecente")
elif edad <= 64:
    print("es un adulto")
elif edad <64:
    print("es un anciano")
else:
    print("la edad no es vaida")