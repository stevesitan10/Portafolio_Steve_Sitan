#Ejercicio
#Dada una lista de números, crea una función llamada sumarPares que reciba una lista y retorne la suma de los números pares que contiene la lista recibida.

#sumarPares([1, 2, 3, 4, 5]) # 6
#sumarPares([10, 20, 30, 40, 50, 60, 70]) # 150
#Tip: Puedes utilizar el operador módulo % para saber si un número es par o impar.

mi solucion: 
def sumarPares(lista):
  conteo = 0
  for i in range(len(lista)):
    if lista[i] % 2== 0:
      conteo = conteo + lista[i]
  return conteo

#solucion alternativa y eficiente

def sumarPares(lista):
    return sum(num for num in lista if num % 2 == 0)
