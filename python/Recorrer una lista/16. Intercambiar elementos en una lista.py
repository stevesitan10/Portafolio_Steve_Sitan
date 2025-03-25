#Intercambiar elementos de una lista
#Podemos intercambiar los elementos de una lista utilizando una de estas dos formas:

#Usando una variable auxiliar:
mi_lista = [1, 2, 3, 4, 5]
# Intercambiar elementos en las posiciones 1 y 3
auxiliar = mi_lista[1]
mi_lista[1] = mi_lista[3]
mi_lista[3] = auxiliar
print(mi_lista)  # [1, 4, 3, 2, 5]
Usando asignación múltiple:
mi_lista = [1, 2, 3, 4, 5]
# Intercambiar elementos en las posiciones 1 y 3
mi_lista[1], mi_lista[3] = mi_lista[3], mi_lista[1]
print(mi_lista)  # [1, 4, 3, 2, 5]

#Ejercicio
#Crea una función llamada intercambiar_elementos que intercambie el primer y último elemento de una lista. La función recibirá una lista y dos enteros que representan las posiciones de los elementos a intercambiar. La función debe devolver la lista con los elementos intercambiados.

#print(intercambiar_elementos([1, 2, 3, 4, 5]))  # [5, 2, 3, 4, 1]
#print(intercambiar_elementos([9, 12, 8, 3, 5]))  # [5, 12, 8, 3, 9]

def intercambiar_elementos(lista, x, y):
  lista[x],lista[y] = lista[y], lista[x]
  return lista

print(intercambiar_elementos([1, 2, 3, 4, 5], 0, 4))
print(intercambiar_elementos([10, 20, 30, 40, 50], 1, 3))
print(intercambiar_elementos(["rojo", "verde", "azul", "amarillo"], 0, 2))
