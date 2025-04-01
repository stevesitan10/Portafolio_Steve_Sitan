#Ejercicio
#Crea la función calcular_promedio que reciba un diccionario con las notas de un curso y retorne el promedio de las notas.

#Ejemplo de ejecución:

#notas = {
#  'Ana': 85,
#  'Luis': 90,
#  'María': 78,
#  'Juan': 92
#}

#calcular_promedio(notas) # 86.25

def calcular_promedio(diccionario):
  lista = diccionario.values()
  return sum(lista)/len(lista)

print(calcular_promedio( {'Ana': 85, 'Luis': 90, 'María': 78, 'Juan': 92}))
