#Ejercicio
#Crea una función llamada calcular_raices que tome una lista de números y devuelva una lista con la raíz cuadrada de cada número. Para esto, debes importar el módulo math y usar la función sqrt().

#calcular_raices([4, 9, 16, 25])  # Debe devolver: [2.0, 3.0, 4.0, 5.0]


from math import sqrt

def calcular_raices(lista):
    return list(map(lambda x: sqrt(x), lista))

print(calcular_raices([4, 9, 16, 25]))
print(calcular_raices([4, 9, 16, 25, 36]))
