#Ejercicio
#Crea una función llamada mensajeOculto que reciba una lista y retorne un texto con el mensaje escondido, utilizando solo la primera letra de cada elemento de la lista con índice par.

#Ejemplo:

#mesajeOculto(["Hoja", "Perro", "Oso", "Gato", "Lana", "", "Arbol"]) # "HOLA"
#Tip: Recuerda la función substring para obtener una subcadena de un string. Tip 2: De la misma forma que sumas números puedes concatenar strings. Tip 3: Necesitas inicializar un string vacío para ir concatenando las letras. Por motivos del ejercicio el cero es considerado un número par.

def mensajeOculto(lista):
  return "".join(lista[x][0:1] for x in range(len(lista)) if x % 2 == 0)

lista = ["Hola", "Mundo"]
print(lista[0][0])  # "H"
print(lista[1][0])  # "M"
