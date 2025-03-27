## otro ejemplo 
def agregar_punto(notas):
  nueva = []
  for nota in notas:
    nueva.append(nota + 1)
  return nueva

original = [4, 5, 7, 2, 3]
nueva = agregar_punto(original)
print(original)  # [4, 5, 7, 2, 3]
print(nueva)  # [5, 6, 8, 3, 4]

#Ejercicio
#Crea una función llamada agregarStock que reciba una lista con las cantidades de cada producto y un número entero que representa la cantidad de stock a agregar a cada producto. La función debe retornar una nueva lista con las cantidades de stock actualizadas.

#Ejemplo:

#agregarStock([10, 20, 30, 40], 5)  # [15, 25, 35, 45]
#Tip: Recuerda usar range(len(lista)) para iterar sobre los índices de la lista.

def agregarStock(lista, numero):
  list2 = list(map(lambda x: x + numero, lista))
  return list2
print(agregarStock([2, 3, 4], 5))
print(agregarStock([5, 5, 6], 3))




