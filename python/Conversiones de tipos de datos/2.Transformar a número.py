#Ejercicio
#Crea una función llamada sumar_datos que reciba una lista y retorne la suma de los elementos de la lista. Si hay algún elemento que no sea un número, debes intentar convertirlo a número antes de sumarlo. Si la conversión no es posible, ignora ese elemento.

#Ejemplo:

#print(sumar_datos([1, "2", 3, "4"]))  # 10
#print(sumar_datos([10, "20", 30, "40", 50, 60, 70]))  # 280

def sumar_datos(lista):
  return sum(float(x) for x in lista)

sumar_datos([10, "20", 30, "40", 50, 60, 70])
sumar_datos([1, "2", 3, "4"])
