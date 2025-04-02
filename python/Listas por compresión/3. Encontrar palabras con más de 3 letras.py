#Ejercicio
#Crea una función llamada filtrar_palabras_cortas que reciba una lista de palabras y devuelva una nueva lista que incluya únicamente las palabras que tengan más de 3 letras. Utiliza una lista por comprensión para realizar esta operación de filtrado.

#Ejemplo de salida esperada:

#palabras = ["casa", "sol", "gato", "en", "Python", "es", "divertido"]
#print(filtrar_palabras_cortas(palabras))  # Debe devolver: ['casa', 'gato', 'Python', 'div

def filtrar_palabras_cortas(lista):
    return list(filter(lambda x: len(x) > 3, lista))


print(filtrar_palabras_cortas(["casa", "sol", "gato", "en", "Python", "es", "divertido"]))
print(filtrar_palabras_cortas(["el", "perro", "come", "un", "hueso", "grande"]))
print(filtrar_palabras_cortas(["a", "ab", "abc", "abcd", "abcde"]))
