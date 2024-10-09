numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# se usa el .reverse para dal vuelta la lista, si empezaba del 1 al 10, empezaradel 10 al 1
numbers.reverse()
for number in numbers:
    #usamos el (end=",") para que a la hora de imprimir se imprima en una sola linea en vez de separados
    print(number, end=", ")