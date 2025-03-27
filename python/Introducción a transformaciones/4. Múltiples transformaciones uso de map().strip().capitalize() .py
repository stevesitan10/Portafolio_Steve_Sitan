#Ejercicio
#Crea una función llamada transformar que reciba una lista de nombres y realice las siguientes transformaciones:

#Eliminar los espacios en blanco al principio y al final de cada nombre.
#Capitalizar la primera letra de cada nombre.
#Agregar un punto al final de cada nombre.
#La función debe modificar la lista original y no retornar nada.
#sobre la siguiente lista de nombres:

#nombres = [" ana", "luis ", " jose", "rosa", "julio "]
#Ejemplo:

#nombres = [" ana", "luis ", " jose", "rosa", "julio "]
#transformar(nombres)
#print(nombres)  # ["Ana.", "Luis.", "Jose.", "Rosa.", "Julio."]
#Tip: Usa los métodos strip(), capitalize(), y la concatenación de strings para realizar las

def transformar(lista):
  lista[:] = map(lambda x: x.strip().capitalize() + ".", lista)
  return lista

nombres = [" ana", "luis ", " jose", "rosa", "julio "]
transformar(nombres)
print(nombres)
