#Ejercicio
#Crea una función llamada imprimir_posiciones_pares que reciba una lista anidada e imprima solo los elementos que están en posiciones pares (tanto i como j pares). La función debe imprimir cada elemento en una nueva línea, precedido por su posición en la forma (i, j).

#lista = [
#    ['a', 'b', 'c', 'd'],
#    ['e', 'f', 'g', 'h'],
#    ['i', 'j', 'k', 'l'],
#    ['m', 'n', 'o', 'p']
#]
#imprimir_posiciones_pares(lista)
# Debe imprimir:
# (0, 0) a
# (0, 2) c
# (2, 0) i
# (2, 2) k

def imprimir_posiciones_pares(lista):
    for i, sublista in enumerate(lista):
        for h, item in enumerate(sublista):
            if i% 2 == 0 and h %2 == 0:
                print(f"({i},{h}) "+ item)
        
