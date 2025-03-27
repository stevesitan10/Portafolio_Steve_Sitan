Ejemplo de split() en Python
La función split() divide una cadena en una lista de palabras usando un separador (por defecto, el espacio " ").

#Ejemplo 1: Dividir una frase en palabras

frase = "Hola mundo Python"
palabras = frase.split()  
print(palabras)  # ['Hola', 'mundo', 'Python']

#Ejemplo 2: Dividir una cadena por comas

datos = "Juan,Pedro,Maria,Ana"
lista_nombres = datos.split(",")
print(lista_nombres)  # ['Juan', 'Pedro', 'Maria', 'Ana']


#Ejemplo 3: Dividir usando un límite de cortes

texto = "Hola mundo Python es genial"
partes = texto.split(" ", 2)  # Solo hace 2 cortes
print(partes)  # ['Hola', 'mundo', 'Python es genial']

#Uso combinado de map() y split()

entrada = "10 20 30 40 50"
numeros = list(map(int, entrada.split()))  
print(numeros)  # [10, 20, 30, 40, 50]
🔹 Explicación:

split() separa "10 20 30 40 50" en ["10", "20", "30", "40", "50"].

map(int, ...) convierte cada string en un número entero.

