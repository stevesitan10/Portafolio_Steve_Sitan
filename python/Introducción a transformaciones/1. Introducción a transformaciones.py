#Ejercicio
#Se tiene una lista con las notas de algunos estudiantes. Crea una función llamada agregar_punto que reciba una lista de notas y que modifique la lista original, agregando 1 punto a cada nota. La función no debe retornar nada, solo modificar la lista original e imprimirla.

#original = [4, 5, 7, 2, 3]
#agregar_punto(original)
#print(original)  # [5, 6, 8, 3, 4]
#Tip: Recuerda usar range(len(notas)) para iterar sobre los índices de la lista.

def agregar_punto(lista):
  
  for x in range(len(lista)):
    lista[x] += 1
  return print(lista)

agregar_punto([2, 3, 4])
agregar_punto([5, 5, 6])





### con uso de map 
#Si deseas usar map(), ten en cuenta que map() devuelve un nuevo iterable y no modifica la lista original. Por lo tanto, necesitas reasignar el resultado a la lista original.
#Aquí tienes la solución usando map():

def agregar_punto(notas):
    notas[:] = list(map(lambda x: x + 1, notas))  # Modifica la lista original

#Explicación:
map(lambda x: x + 1, notas):
Usa lambda para sumar 1 a cada elemento de la lista.
map() devuelve un iterable, por lo que lo convertimos en una lista con list().
notas[:] = ...:
notas[:] moifica la lista en el lugar (in-place), sin crear una nueva.
Esto asegura que la lista original se actualice. 🚀
