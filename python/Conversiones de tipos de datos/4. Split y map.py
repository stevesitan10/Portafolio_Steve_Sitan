#Ejercicio
#Crea una función llamada sumar_datos que reciba un string, lo convierta en una lista y luego sume los elementos de la lista. La función debe retornar la suma de los elementos.

#Ejemplo:

#print(sumar_datos("1,2,3,4"))  # 10
#*Tip: Debes convertir los elementos de la lista a números antes de sumarlos.

def sumar_datos(lista):
  return sum(list(map(int,lista.split(","))))

print(sumar_datos("10,2,1,3,9"))
