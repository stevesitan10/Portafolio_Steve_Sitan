#Ejercicio
#Crea una función llamada desde_hasta que reciba tres parámetros:

#Una lista de números
#Un índice de inicio desde
#Un índice de fin hasta
#La función debe mostrar los elementos de la lista desde el índice de inicio desde hasta el índice hasta (sin incluir el elemento en el índice hasta).

#Ejemplo:

#desde_hasta([1, 2, 3, 4, 5, 6], 2, 4)
#"""
#3
#4
#"""

def desde_hasta(lista, desde, hasta):
    i = desde
    
    while i < hasta  :
        print(lista[i])
        i = i + 1
        
