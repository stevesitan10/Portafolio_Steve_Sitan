#Ejercicio
#Crea una función numeros_dobles que genere una lista por comprensión de los primeros x números multiplicados por 2, donde el valor de x es un parámetro de la función. La función debe devolver la lista.

#Ejemplo de salida esperada:

#print(numeros_dobles(3))  # Debe devolver: [2, 4, 6]
#print(numeros_dobles(5))  # Debe devolver: [2, 4, 6, 8, 10]

def numeros_dobles(numero):
    return list(x*2 for x in range(1,numero+1))

print(numeros_dobles(3))
print(numeros_dobles(5))
print(numeros_dobles(10))
