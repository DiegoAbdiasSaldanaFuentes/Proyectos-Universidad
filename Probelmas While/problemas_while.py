# Autor: Diego Saldaña
# Fecha: 14/08/2024

import os

"""
contador =  0
while contador <= 100:
    print(contador)
    contador += 1"""

"""# tabla de multiplicar con bucle for
numero = int(input("ingrese un numero:"))
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")"""


"""#tabla de multiplicar pero con While
numero = int(input("ingrese un numero:"))
contador = 1

while contador <=10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1"""

"""#cuenta regresiva
numero = int(input("ingrese su numero:"))
while numero  != 0:
    print(numero)
    numero -= 1
print("DESPEGUEN")"""


palabra = input("Ingresa una palabra: ")
indice = 0

while indice < len(palabra):
    print(palabra[indice])
    indice += 1

