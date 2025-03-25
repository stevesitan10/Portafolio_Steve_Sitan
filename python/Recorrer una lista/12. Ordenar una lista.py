#Ejercicio
#Crea una función llamada primeros_x que reciba dos parámetros: una lista y una cantidad elementos. La función debe devolver una lista con los primeros x elementos de la lista ordenados de forma ascendente.

#Ejemplo:

#print(primeros_x([4, 6, 8, 2, 3], 2))  # [2, 3]
#print(primeros_x([1, 9, 3, 4, 5, 2], 4))  # [1, 2, 3, 4]
#print(primeros_x(["manzana", "banana", "cereza"], 2))  # ['banana', 'cereza']

def primeros_x(numeros, x):
  return sorted(numeros[:x])

print(primeros_x([7, 5, 3, 9, 1], 3)) 
print(primeros_x(["zorro", "elefante", "gato", "ballena"], 3))  
print(primeros_x([14, 3, 25, 8, 20], 4)) 
