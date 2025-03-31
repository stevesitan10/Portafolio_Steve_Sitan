#Ejercicio
#Crea una función llamada combinar_tuplas que reciba dos tuplas y las combine de la siguiente manera:

#Agrega el contenido de la primera tupla.
#Agrega el contenido de la segunda tupla.
#Agrega el contenido de la segunda tupla.
#Agrega el contenido de la primera tupla.
#La función debe devolver la nueva tupla con el contenido combinado.

#Ejemplo de uso:

#semestre1 = ("Francisca", "Camila")
#semestre2 = ("Javier", "Felipe")
#print(combinar_tuplas(semestre1, semestre2)) # Debe mostrar: ("Francisca", "Camila", "Javier", "Felipe", "Jav

def combinar_tuplas(tupla1, tupla2):
  tupla3 = tupla1 + tupla2 + tupla2 + tupla1
  return tupla3

print(combinar_tuplas(("Programación", "Álgebra"),("Estadística", "Inglés")))
print(combinar_tuplas((1, 2, 3),(4, 5, 6)))
