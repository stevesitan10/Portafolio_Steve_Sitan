#Ejercicio
#Crea la función encontrar_stock que reciba un diccionario con el inventario de una tienda y retorne la cantidad total de productos en stock.

#invetario = {
#  'manzanas': 50,
#  'peras': 30,
#  'naranjas': 75,
#  'uvas': 25
#}

#encontrar_stock(inventario) # 180
#Tip: Una vez que obtengas los valores del diccionario puedes iterar sobre ellos y sumarlos uno a uno utilizando un bucle for o cualquier otra técnica que prefieras.

def encontrar_stock(Diccionario):
  return  sum(list(Diccionario.values()))

print(encontrar_stock({'manzanas': 50, 'peras': 30, 'naranjas': 75, 'uvas': 25}))
print(encontrar_stock({'laptop': 10, 'celular': 50, 'tablet': 25, 'smartwatch': 15}))
