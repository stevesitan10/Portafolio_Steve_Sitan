#Ejercicio
#Crea una función llamada procesar_palabras que tome una lista de palabras como parámetro y devuelva una nueva lista que:

##Contenga solo las palabras que tienen más de 3 letras (filtrado)
#Convierta estas palabras a mayúsculas (transformación)
#Añada la longitud de la palabra al final, separada por un guion (transformación adicional)
#Utiliza una lista por comprensión para realizar estas operaciones de filtrado y transformación.

#Ejemplo de salida esperada:

#palabras = ["sol", "luna", "estrella", "planeta", "cometa", "galaxia"]
#print(procesar_palabras(palabras))  # Debe devolver: ['LUNA-4', 'ESTRELLA-8', 'PLANETA-7',
def procesar_palabras(lista):
    return list(x.upper() + "-" + str(len(x)) for x in lista if len(x) > 3 )

#Alternativa
def procesar_palabras(lista):
    filtro = list((filter(lambda x: len(x) > 3, lista)))
    return list(map(lambda x: x.upper() + "-" + str(len(x)), filtro))

print(procesar_palabras(["sol", "luna", "estrella", "planeta", "cometa", "galaxia"]))
print(procesar_palabras(["el", "perro", "come", "un", "hueso", "grande"]))
print(procesar_palabras(["a", "ab", "abc", "abcd", "abcde", "abcdef"]))
