#Ejercicio
#Crea una función lambda que concatene dos cadenas de texto con un guion entre ellas y asígnala a la variable concatenador.

#Ejemplo de uso: concatenador("Hola", "mundo") # Debe retornar "Hola-mundo" concatenador("Hola", "amigo") # Debe retornar "Hola-amigo"

concatenador = lambda x, y: x + "-" + y
print(concatenador("Hola", "mundo"))
print(concatenador("Hola", "amigo"))
