#Ejercicio
#Crea una función llamada sumar_datos que reciba una lista como parámetro y retorne la suma de todos sus elementos excepto el primero y el último. La lista siempre tendrá al menos tres elementos.

#Ejemplo:

#print(sumar_datos([1, 2, 3, 4, 5]))  # 9
#print(sumar_datos([4, 6, 8, 2, 3]))  # 16


def sumar_datos(lista):
  return sum(lista[1:-1])

print(sumar_datos([4,6,8,2,3]))
print(sumar_datos([1,2,3,4,5,6,7,8]))
print(sumar_datos([10,11,12,13]))
