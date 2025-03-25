#Forma #1 de contar

#numeros = [1, 5, 3, 4, 5]
#contador = 0
#for numero in numeros:
#  if numero == 5:
#    contador += 1
#print(contador) # Debe mostrar: 2
#Podemos resolver el mismo problema utilizando while

#Forma #2
#numeros = [1, 5, 3, 4, 5]
#contador = 0
#i = 0
#while i < len(numeros):
#  if numeros[i] == 5:
#    contador += 1
#  i += 1

Ejercicio
Crea una función llamada contar_cinco. Esta función debe recibir una lista de números y retornar la cantidad veces que aparece el número 5 en esa lista.

Ejemplo de cómo debe funcionar:

print(contar_cinco([1, 5, 3, 4, 5]))  #  2
print(contar_cinco([5, 5, 5, 2, 1]))  # 3
Consejo: no olvides empezar tu contador en cero antes de mirar los números de la lista.

#solucion 

  def contar_cinco(lista):
  conteo = 0
  for numero in lista:
    if numero == 5:
      conteo = conteo + 1
  return conteo 

print(contar_cinco([1, 5, 3, 4, 5]))
print(contar_cinco([5, 5, 5, 2, 1]))
print(contar_cinco([1, 2, 3, 4, 6, 7, 8, 9]))
  
