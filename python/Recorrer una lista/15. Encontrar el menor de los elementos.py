#Ejercicio
#Crea una función llamada encontrar_minimo que reciba una lista de números como parámetro. La función debe retornar el número menor de la lista.

#Ejemplo:

#print(encontrar_minimo([1, 5, 8, 3, 2]))  # 1
#print(encontrar_minimo([-5, -10, -2, -1]))  # -10
#Asume que la lista siempre contendrá al menos un elemento.

def encontrar_minimo(lista):
  minimo = lista[0]
  for numero in lista:
    if numero < minimo:
      minimo = numero 
  return minimo 
  
print(encontrar_minimo([1, 5, 8, 3, 2]))
print(encontrar_minimo([-5, -10, -2, -1]))
print(encontrar_minimo([100, 0, 50, 75, 120, 25]))
