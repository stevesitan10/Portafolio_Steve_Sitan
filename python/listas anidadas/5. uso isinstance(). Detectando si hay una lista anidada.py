#Ejercicio
#Crea una función llamada tiene_lista_anidada que reciba una lista como argumento y retorne True si la lista contiene al menos una lista anidada, y False en caso contrario.

#print(tiene_lista_anidada([1, 2, 3, 4]))  # Debe imprimir: False
#print(tiene_lista_anidada([1, 2, [3, 4], 5]))  # Debe imprimir: True
#print(tiene_lista_anidada([1, 2, "hola", [3, 4]]))  # Debe imprimir: True
#Tip: Puedes usar un bucle for para recorrer la lista y la función isinstance(elemento, list) para verificar si cada elemento es una lista.

def tiene_lista_anidada(lista):
    for items in lista:
        if isinstance(items, list) == True:
            return True
    return False

print(tiene_lista_anidada([1, 2, 3, 4, 5]))
print(tiene_lista_anidada([1, [2, 3], 4, 5]))
