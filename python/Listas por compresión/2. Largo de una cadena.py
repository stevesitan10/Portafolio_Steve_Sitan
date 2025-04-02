Ejercicio
Crea una función llamada contar_largo que tome una lista de strings como parámetro y devuelva una nueva lista que indique el largo de cada string. Utiliza una lista por comprensión para realizar esta operación.

Ejemplo de salida esperada:

datos = ["hola", "python", "es", "genial"]
print(contar_largo(datos))  # Debe devolver: [4, 6, 2, 6]

def contar_largo(lista):
    return list(len(x) for x in lista)

print(contar_largo(["hola", "python", "es", "genial"]))
print(contar_largo(["ejemplo 1", "texto de prueba", "otro caso"]))
