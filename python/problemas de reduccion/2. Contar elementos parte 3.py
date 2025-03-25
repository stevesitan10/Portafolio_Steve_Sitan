Ejercicio
Crea una función llamada contar_numero que reciba dos parámetros: una lista de números y el número que se desea contar. La función debe retornar la cantidad de veces que aparece el número especificado en la lista.

Ejemplo:

print(contar_numero([1, 5, 3, 4, 5], 5))  # 2
print(contar_numero([1, 2, 3, 2, 4, 2], 2))  # 3
print(contar_numero([1, 2, 3, 4, 5], 6))  # 0
Tip: Recuerda que la función debe ser capaz de contar cualquier número, no solo un número específico como en el ejercicio anterior.

##solucion 

def contar_numero(lista, x):
  contador = 0
  for numero in lista:
    if numero == x:
      contador += 1
  return contador

print(contar_numero([1, 5, 3, 4, 5], 5))
print(contar_numero([1, 2, 3, 2, 4, 2], 2))
print(contar_numero([1, 2, 3, 4, 5], 6))
