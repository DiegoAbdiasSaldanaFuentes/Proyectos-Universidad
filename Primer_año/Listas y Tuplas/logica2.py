#algoritmo que nos preguntara cuales son los numeros ganadores en un kino
#lista vacia donde almacenaremos los numero ganadores
awarded = []
#creamos un bucle que en un rango de 6, nos pregunte 6 veces cuales son nuestros numeros ganadores
for i in range(6):
    #realizamo un appen a la lista que es un input que nos pregunta cuales son los numeros y los guardara en la lista vacia
    awarded.append(int(input("Introduce un número ganador: ")))
# modificamo la lista usando el sort para que los ordene de menor a mayor predeterminadamente
awarded.sort()
#creamo la salida ytransformamo los numeros ganadores sstring
print("Los números ganadores son " + str(awarded))