#Ejercicio
#Crea una función llamada mostrar que reciba una lista de números y que muestre los primeros 3 números de la lista utilizando un ciclo while. Considera que todos los casos de prueba tienen al menos 3 elementos. Ejemplo:

#mostrar([1, 2, 3, 4, 5, 6])
#"""
#1
#2
#3
#"""
#mostrar([10, 20, 30, 40, 50, 60, 70])
#"""
#10
#20
#30
#"""
#Tip: Recuerda que cuando se pide mostrar, no debes retornar nada, solo mostrar los datos utilizando print. Asegúrate de usar un ciclo while para esta tarea.

def mostrar(lista):
    i = 0
    while i < 3:
        print(lista[i])
        i = i + 1

mostrar([4,6,8,2,3])

#Respuesta
4
6
8

