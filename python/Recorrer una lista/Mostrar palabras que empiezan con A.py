#Ejercicio
#Crea una función llamada mostrarLasPalabrasQueEmpiezanConA que reciba un arreglo de palabras y muestre las palabras que empiezan con la letra "a".

#Ejemplo
#MostrarLasPalabrasQueEmpiezanConA(["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"])
#"""
#amet
#adipiscing
#"""

def mostrarLasPalabrasQueEmpiezanConA(cadena):
    i = 0
    for i in range(1,len(cadena)):
        x = cadena[i]
        if x[0:1] == "a":
            print(cadena[i])

##########################################################
#Alternativa #1

def mostrarLasPalabrasQueEmpiezanConA(cadena):
    for i in range(len(cadena)):
      if cadena[i].startswith("a"):
            print(cadena[i])
##########################################################
#Alternativa #2 (más eficiente)
def mostrarLasPalabrasQueEmpiezanConA(cadena):
    for i in cadena:
      if i.startswith("a"):
            print(i)

mostrarLasPalabrasQueEmpiezanConA(["manzana", "arándanos", "naranja", "pera", "uva"])
mostrarLasPalabrasQueEmpiezanConA(["gato", "perro", "ardilla", "pez", "conejo", "alce"])
mostrarLasPalabrasQueEmpiezanConA(["rojo", "azul", "verde", "amarillo"])
        
        
