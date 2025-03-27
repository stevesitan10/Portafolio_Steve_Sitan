#Cómo usar map() en Python
#La función map() aplica una función a cada elemento de un iterable (como una lista o tupla) y devuelve un nuevo iterable con los resultados.

Sintaxis
map(funcion, iterable)
funcion: Es la función que se aplicará a cada elemento del iterable.

#iterable: Es la lista, tupla u otro iterable cuyos elementos serán transformados.

🔹 Nota: map() devuelve un objeto iterable. Si quieres verlo como una lista, usa list(map(...)).

#Ejemplos básicos de map()
#Ejemplo 1: Elevar al cuadrado cada número de una lista}
numeros = [1, 2, 3, 4, 5]
resultado = map(lambda x: x**2, numeros)
print(list(resultado))  # [1, 4, 9, 16, 25]



#Ejemplo 2: Convertir una lista de cadenas a mayúsculas
palabras = ["hola", "mundo", "python"]
mayusculas = map(str.upper, palabras)
print(list(mayusculas))  # ['HOLA', 'MUNDO', 'PYTHON']




#Ejemplo 3: Sumar dos listas elemento a elemento
Si map() recibe dos listas, aplicará la función a los pares de elementos de ambas listas.
  lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
suma = map(lambda x, y: x + y, lista1, lista2)
print(list(suma))  # [5, 7, 9]



#Uso combinado con split()
#Podemos procesar una entrada de números separada por espacios y convertirlos en enteros usando map().

entrada = "10 20 30 40 50"
numeros = list(map(int, entrada.split()))
print(numeros)  # [10, 20, 30, 40, 50]
