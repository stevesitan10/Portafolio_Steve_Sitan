#Ejercicio
#Crea una función llamada cambiar_valor que reciba como argumento un diccionario, una clave y un valor. Cambia el valor asociado a la clave en el diccionario y luego retorna el diccionario modificado.

#Ejemplo de ejecución:

#print(cambiar_valor({"nombre": "Juan", "edad": 25}, "nombre", "Pedro"))
# {"nombre": "Pedro", "edad": 25}

def cambiar_valor(diccionario, key, item):
  diccionario[key] = item
  return diccionario

print(cambiar_valor({"nombre": "Juan", "edad": 25}, "nombre", "Pedro"))
print(cambiar_valor({"nombre": "Juan", "edad": 25}, "edad", 30))
