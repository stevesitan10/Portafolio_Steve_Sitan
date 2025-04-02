##Uso de map
#Podemos usar map() con funciones definidas previamente:

#def cuadrado(x):
#    return x ** 2

#numeros = [1, 2, 3, 4, 5]
#resultado_map = map(cuadrado, numeros)
#print(list(resultado_map))  # Imprime: [1, 4, 9, 16, 25]
#En este ejemplo, map aplica la función cuadrado a cada elemento de la lista numeros. El resultado es un objeto map, que es un iterador. Podemos convertir este iterador en una lista con los resultados usando list().

#También podemos usar métodos integrados o funciones de la biblioteca estándar:

#palabras = ['hola', 'mundo', 'python']
#resultado_map = map(str.upper, palabras)
#print(list(resultado_map))  # Imprime: ['HOLA', 'MUNDO', 'PYTHON']

def formatear_nombres(lista):
    return list(map(str.lower,lista))

print(formatear_nombres( ["ANA", "juan", "MaRia", "CARLOS"]))
print(formatear_nombres(["PEDRO", "luisa", "FernAnDO", "sofia"]))
print(formatear_nombres( ["jULIA", "MARTIN", "alejandro", "CARMEN"]))
