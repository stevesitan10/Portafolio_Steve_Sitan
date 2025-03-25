#Ejercicio
#Crea una función llamada mostrarPalabrasQueEmpiecenCon que reciba un arreglo de palabras y una letra. El programa debe mostrar en consola las palabras que empiecen con la letra recibida.

#Ejemplo
#mostrarPalabrasQueEmpiecenCon(["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"], "a")

# amet
# adipiscing

#mostrarPalabrasQueEmpiecenCon(["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"], "c")

# consectetur

def mostrarPalabrasQueEmpiecenCon(cadena, letra):
  for palabra in cadena:
    if palabra.startswith(letra): 
      print(palabra)

mostrarPalabrasQueEmpiecenCon(["manzana", "maracuyá", "naranja", "pera", "uva"], "m")
mostrarPalabrasQueEmpiecenCon(["gato", "perro", "ardilla", "pez", "conejo", "camello"], "c")
mostrarPalabrasQueEmpiecenCon(["rojo", "azul", "verde", "amarillo"], "a")
