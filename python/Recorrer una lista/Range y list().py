#Ejercicio
#Crea una función llamada multiplos_de_5 que reciba dos parámetros: inicio y fin y devuelva una lista con los múltiplos de 5 en el rango de inicio a fin (sin incluir fin).

#Ejemplo:

#print(multiplos_de_5(10, 30))  # [10, 15, 20, 25]
#print(multiplos_de_5(3, 24)) # [5, 10, 15, 20]
#Tips: No necesitas revisar divisores, basta con que uses de forma inteligente la función range().

def multiplos_de_5(inicio, fin):
  if inicio % 5 != 0:
        inicio += (5 - (inicio % 5))
  return list(range(inicio, fin, 5))

print(multiplos_de_5(10,30))
print(multiplos_de_5(3,24))
print(multiplos_de_5(2,20))
