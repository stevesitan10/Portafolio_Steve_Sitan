#Ejercicio
#Crea una función llamada filtrar_mayores_a_diez que reciba una lista de números y retorne una nueva lista que contenga solo los números mayores a 10 de la lista original.

##numeros = [5, 15, 3, 20, 8, 12, 1, 25]
#resultado = filtrar_mayores_a_diez(numeros)
#print(resultado)  # Debe mostrar: [15, 20, 12, 25]
#Tip: Utiliza una condición en el if para comprobar si cada número es mayor que 10.

def filtrar_mayores_a_diez(lista):
  return list(filter(lambda x: x > 10, lista))

print(filtrar_mayores_a_diez([8, 11, 15, 3, 20, 9, 10]))
print(filtrar_mayores_a_diez([1, 5, 12, 18, 2, 30, 10, 15]))

#Otro ejemplo: Filtrar palabras cortas
#Filtrar palabras con menos de 5 letras de una lista:

palabras = ["sol", "casa", "elefante", "luz", "montaña", "pez"]

cortas = list(filter(lambda palabra: len(palabra) < 5, palabras))
print(cortas)  # ['sol', 'casa', 'luz', 'pez']
#Aquí, filter() deja solo las palabras con menos de 5 caracteres.
