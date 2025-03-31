#Ejercicio
#Crea una función llamada sumar_lista_anidada que reciba una lista anidada (una lista que contiene otras listas) y retorne la suma de todos sus elementos numéricos.

#lista_anidada = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]
#print(sumar_lista_anidada(lista_anidada))  # Debe mostrar: 45
#Puedes asumir que la lista exterior contendrá solo listas y las listas internas solo números.

def sumar_lista_anidada(lista):
    return sum(sum(sublista) for sublista in lista)


###################################################
#alternativa
def sumar_lista_anidada(lista):
    conteo = 0
    for sublista in lista:
        for item in sublista:
            conteo += item
    return conteo

print(sumar_lista_anidada([[1, 2], [3, 4]]))
print(sumar_lista_anidada([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
