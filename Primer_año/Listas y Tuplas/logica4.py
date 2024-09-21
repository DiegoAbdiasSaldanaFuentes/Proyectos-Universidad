#se crea una lista con las asignatura pedidas
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# se crea una lista vacia 
passed = []
# creamos un bucle que itera los elemento de nuestra lista preguntandonos ¿Que nota no hemos sacado?
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    # luego de haber mencionado nuetras notas pasara por una condicional que se preguntara si nuestras notas on mayores o igual a 5
    if score >= 5:
        #si esta condicion se cumpple las notas que  cumplen son agregada a la lista
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))