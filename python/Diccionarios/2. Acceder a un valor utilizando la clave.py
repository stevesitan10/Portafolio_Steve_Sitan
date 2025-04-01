#Ejercicio
#Crea una función llamada retornar_valor que reciba como argumento un diccionario y un string llave y retorne el valor asociado a la llave en el diccionario estudiante.

#retornar_valor({"nombre": "Juan", "edad": 25}, "nombre") # Juan
#retornar_valor({"nombre": "Juan", "edad": 25}, "edad") # 25

def retornar_valor(diccionario, key):
  estudiante= diccionario.get(key)
  return estudiante

print(retornar_valor({"nombre": "Juan", "edad": 25}, "nombre"))
print(retornar_valor({"nombre": "Juan", "edad": 25}, "edad"))
