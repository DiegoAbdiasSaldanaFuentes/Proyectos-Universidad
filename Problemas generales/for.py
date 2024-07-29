numero_1 = int(input("ingrese un numero:"))
numero_2 = int(input("ingrese un numero:"))
operador = str(input("ingrese un oeprador 'sum', 'mult', 'rest', 'divi':")).lower()
def calculadora (numero_1, numero_2, operador):
    if operador == "sum":
        resultado = numero_1 + numero_2
    elif operador == "mult":
        resultado = numero_1 * numero_2
    elif operador == "rest":
        resultado = numero_1 - numero_2
    elif operador == "divi":
        resultado = numero_1 / numero_2
    else:
        print("el valor que ingreso es invalido")
    
    return resultado

resultado = calculadora(numero_1, numero_2, operador)

print(resultado)
  

