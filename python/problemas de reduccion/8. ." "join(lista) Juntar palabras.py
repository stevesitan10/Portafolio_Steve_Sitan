#Ejercicio
#Crea una función llamada juntarPalabras que reciba una lista de palabras y retorne un string con todas las palabras concatenadas con un espacio entre cada palabra. Al final del string no debe haber un espacio.

#Ejemplo:

#juntarPalabras(["Hola", "Mundo"]) # "Hola Mundo"
#juntarPalabras(["Mensaje", "de", "prueba"]) # "Mensaje de prueba"

def juntarPalabras(lista):
  return " ".join(lista)

#Solucion alternativa

  text = ""
  for palabra in lista:
    text = text+ palabra + " "
  return text

print(juntarPalabras(["Buenos", "días", "a", "todos"]))
print(juntarPalabras(["Vamos", "a", "comenzar"]))
print(juntarPalabras(["Yo", "soy", "tu", "padre"]))
