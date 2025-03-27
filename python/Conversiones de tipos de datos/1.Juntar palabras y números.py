#Ejercicio
#Crea una función llamada juntarPalabras que reciba una lista de palabras y números, y retorne un string con todas las palabras concatenadas con un espacio entre cada palabra. Al final del string no debe haber un espacio.

#Ejemplo:

#juntarPalabras(["Hola", "Mundo", 42]) # "Hola Mundo 42"
#juntarPalabras(["Mensaje", "de", "prueba nº", 100]) # "Mensaje de prueba nº 100"

def juntarPalabras(lista):
  return  " ".join(str(x) for x in lista)

print(juntarPalabras(["Hola", "Mundo", 42]))
print(juntarPalabras(["Mensaje", "de", "prueba nº", 100]))
print(juntarPalabras([10, 20, 30, "Hola", "Mundo"]))
