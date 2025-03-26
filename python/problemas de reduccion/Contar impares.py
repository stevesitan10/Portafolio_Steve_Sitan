#Ejercicio
#Crea una función llamada contarImpares que reciba una lista y retorne la cantidad de números pares que contiene la lista recibida.

#contarImpares([1, 2, 3, 4, 5]) # 3
#contarImpares([10, 20, 30, 40, 50, 60, 70]) # 0

def contarImpares(lista):
  conteo = 0
  for numero in lista:
    if numero % 2 != 0:
      conteo += 1
      
  return conteo

print(contarImpares([4,6,8,2,5]))
print(contarImpares([1,2,3,4,5,6,7,9]))
print(contarImpares([10,11,12,13,15]))
