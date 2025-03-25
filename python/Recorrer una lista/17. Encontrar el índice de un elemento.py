4 formas de iterar con índice en python

Con while, ejemplo:
i = 0
while i < len(values):
    print(i, values[i])
    i += 1


Con for y un contador:
i = 0
for ele in values:
    print(i, ele)
    i += 1


3 Con for y range:

for i in range(len(values)):
    print(i, values[i])


Con for y enumerate:
for i, value in enumerate(values):
  print(i, value)
Todas pueden resolver el problema.

Ejercicio
La función encontrar_indice debe buscar el elemento en el arreglo y devolver su índice. Si el elemento no se encuentra en el arreglo, la función debe devolver None.

Tu tarea es completar el cuerpo de la función para que funcione correctamente.

Ejemplos de cómo debería funcionar la función:

print(encontrar_indice([1, 3, 5, 7, 9], 5))  # Debería retornar: 2
print(encontrar_indice([1, 3, 5, 7, 9], 6))  # Debería retornar: None
print(encontrar_indice(["a", "b", "c"], "b"))  # Debería retornar: 1
Tip: Puedes usar un bucle for con la función range() para acceder tanto al índice como al elemento en cada iteración.


def encontrar_indice(arreglo, elemento):
  for i in range(len(arreglo)):
    if arreglo[i] == elemento:
      return i 
  return None

print(encontrar_indice([1, 3, 5, 7, 9], 5))
print(encontrar_indice([1, 3, 5, 7, 9], 6))
print(encontrar_indice(["a", "b", "c"], "b"))
