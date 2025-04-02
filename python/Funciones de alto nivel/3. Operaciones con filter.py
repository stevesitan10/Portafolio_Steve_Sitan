#Ejercicio
#Crea una función llamada filtrar_mayores_que que reciba una lista de números y un valor límite. La función debe utilizar filter() con una función lambda para devolver una nueva lista que contenga solo los números mayores que el valor límite.

#Ejemplo:

#print(filtrar_mayores_que([1, 5, 10, 15, 20], 10))  # Debe devolver: [15, 20]

def filtrar_mayores_que(lista, limite):
    return list(filter(lambda x: x > limite, lista))

print(filtrar_mayores_que([1, 5, 10, 15, 20], 10))
print(filtrar_mayores_que( [-5, 0, 5, 10, 15], 0))
print(filtrar_mayores_que([100, 200, 300, 400, 500], 250))
