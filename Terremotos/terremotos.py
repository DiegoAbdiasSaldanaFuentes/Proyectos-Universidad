# Autor: Diego Saldaña
# Fecha: 18/08/2024
# Version: 0.0




# entradas de datos
def leer_datos(i):
    ent = open(i)
    datos = []
    for linea in ent:
        linea = linea.rstrip("\n")
        separador = linea.split(" ")
        datos.append(separador)
    ent.close()
    return datos

# indica la fecha y hora del mayor sismo registrado
def funcion_a(datos):
    max_sismo = max(datos, key=lambda x: float(x[4]))
    return max_sismo


if __name__ == "__main__":
    lectura_datos = leer_datos("terremotos_datos.txt")
    fecha_hora_mayor_registrado = funcion_a(lectura_datos)

print(fecha_hora_mayor_registrado)