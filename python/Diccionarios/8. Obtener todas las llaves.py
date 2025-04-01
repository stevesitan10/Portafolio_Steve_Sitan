#Ejercicio
#Crea la función contar_productos que reciba un diccionario con el inventario de una tienda y retorne la cantidad total de tipos de productos diferentes en el inventario.

#inventario = {
#'manzanas': 50,
#'peras': 30,
#'naranjas': 75,
#'uvas': 25
#}
#contar_productos(inventario) # 4

def contar_productos(diccionario):
  return len(list(diccionario.keys()))

print(contar_productos({'manzanas': 50, 'peras': 30, 'naranjas': 75, 'uvas': 25}))
print(contar_productos({'laptop': 10, 'celular': 50, 'tablet': 25, 'smartwatch': 15, 'auriculares': 100}))
