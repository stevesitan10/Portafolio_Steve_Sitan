#Ejercicio
#Crea una función llamada mostrarDatosAlReves que reciba un arreglo y que muestre los datos del arreglo en orden inverso.

#Ejemplo:

#mostrarDatosAlReves([1, 2, 3, 4, 5]) 
#/* 
#5
#4
#3
#2
#1
#*/

def mostrarDatosAlReves(lista):
    n = len(lista) 
    i = 1
    while i <= n:
        recorrido = n - i
        print(lista[recorrido])
        i = i +1


mostrarDatosAlReves([4,6,8,2,3])
mostrarDatosAlReves([1,2,3,4,5,6,7,8])
mostrarDatosAlReves([10,11,12,13])
