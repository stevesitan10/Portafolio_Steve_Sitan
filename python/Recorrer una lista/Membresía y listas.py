#Ejercicio
#Crea una función llamada contar_presentes que reciba dos listas como parámetros: una lista de elementos a buscar y una lista donde buscar. La función debe devolver el número de elementos de la primera lista que están presentes en la segunda lista.

#Ejemplo:

#frutas = ["manzana", "banana", "cereza", "dátil", "uva"]
#buscar1 = ["manzana", "kiwi", "cereza"]
#buscar2 = ["pera", "sandía", "mango", "uva"]

#print(contar_presentes(buscar1, frutas))  # 2
#print(contar_presentes(buscar2, frutas))  # 1

def contar_presentes(lista1, lista2):
  x = 0
  for palabra in lista1:
    if palabra in lista2:
      x = x + 1
  return x

print(contar_presentes(["a","b","c"],["x","y","z","a","b"])) 
print(contar_presentes([1,2,3,4],[1,3,5,7,9])) 
print(contar_presentes(["rojo","verde","azul"],["amarillo","verde","naranja","azul"])) 
