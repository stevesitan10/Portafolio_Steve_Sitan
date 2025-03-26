
#Ejercicio
#Crea una función llamada calcular_promedio que reciba 2 parámetros, lista1 y lista2 y devuelva el promedio de los elementos de ambas listas.

#Ejemplo:

#print(calcular_promedio([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))  # 5.5
#print(calcular_promedio([4, 6, 8, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8]))  # 4.5

def calcular_promedio(lista1, lista2):
   suma = sum(lista1) + sum(lista2)
   promedio = suma/(len(lista1)+len(lista2))
   return promedio

print(calcular_promedio([1,2,3], [4,5,6]))
print(calcular_promedio([1,2], [3,4]))
