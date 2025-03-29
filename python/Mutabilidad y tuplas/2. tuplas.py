#Ejercicio
#Crea una función llamada info_estudiante que reciba el nombre, edad y promedio de un estudiante como argumentos separados. La función debe retornar una tupla con esta información.

#print(info_estudiante("Ana", 20, 8.5)) # ("Ana", 20, 8.5)
#Tip: Recuerda que puedes crear una tupla simplemente separando los valores con comas. Para acceder a los elementos de la tupla, usa los índices [0], [1], [2], etc.

def info_estudiante(nombre, edad, promedio):
  tupla = nombre,edad,promedio
  return tupla

print(info_estudiante("Ana", 20, 8.5))
print(info_estudiante("Juan", 19, 8.5))
