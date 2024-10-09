
#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura,
#  y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
# es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

#paso, dividir para reinar; separo en lo que me pide; preguntar al usuario, crear una lista y despues crear salida

# se crea una lista con los elementos
asignaturas = ["matematicas","fisica","quimica","historia","lenguaje"]

#creamos una lista vacia donde agregaremos nuestros resultados
noto = []
#creamos un bucle para que itere elemento por elemento preguntandonos "¿Que nota se ah sacado"
for elem in asignaturas:
    #creamos una variable que nos permita preguntar al usuario que nota se ah acado en cada elemento (se repetira la pregunta con todos los elementos)
    a = input(f"¿Qué nota te has sacado en {elem}?:")
    #realizamos un append porque el append agrega los elementos en una variable o una lista en este caso
    noto.append(a)

#creamos una variable (i) que esta iterara por cada len en aignatura el len cuenta cuanto elementos posee cada caracter y como las listas son un caracter
#contara solo 5 porque son 5 elementos que hay, y seguira el bucle 5 veces
for i in range(len(asignaturas)):
    #creamos la salida que nos mostrara las asiganturas y especificamo que muestre las aignaturas pero en base a (i) porque el algoritmo repetira mucha veces el resultado
    # y en la variable "noto"  especificamo el (i) porque si ni este mostrara la lista completa
    print(f"tu nota en {asignaturas[i]} es de {noto[i]}")





