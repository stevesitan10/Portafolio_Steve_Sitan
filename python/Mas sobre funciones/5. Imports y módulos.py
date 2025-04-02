from math import sqrt

def calcular_raices(lista):
    return list(map(lambda x: sqrt(x), lista))

print(calcular_raices([4, 9, 16, 25]))
print(calcular_raices([4, 9, 16, 25, 36]))
