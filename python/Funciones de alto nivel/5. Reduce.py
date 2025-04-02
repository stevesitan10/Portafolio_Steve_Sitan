#Ejercicio
#Crea una función llamada calcular_producto que reciba una lista de números. La función debe usar reduce() junto con una función lambda para calcular y retornar el producto de todos los números en la lista.

#Ejemplo:

#print(calcular_producto([1, 2, 3, 4, 5]))  # Debe devolver: 120
#Tip: Recuerda importar reduce del módulo functools.

from functools import reduce

def calcular_producto(lista):
    return reduce(lambda x,y: x*y, lista)

print(calcular_producto([1, 2, 3, 4, 5]))
print(calcular_producto([2, 3, 4]))
print(calcular_producto([1, 10, 100]))
