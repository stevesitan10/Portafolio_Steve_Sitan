#Ejercicio
#Crea una función llamada mostrar_tabla que reciba un número y muestre la tabla de multiplicar de ese número del 1 al 10. La función no debe retornar nada, solo mostrar los resultados.

#Ejemplo de cómo debería funcionar:

#mostrar_tabla(5)
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#5 x 4 = 20
#5 x 5 = 25
#5 x 6 = 30
#5 x 7 = 35
#5 x 8 = 40
#5 x 9 = 45

def mostrar_tabla(numero):
  for i in range(1, 11):
    resultado = i * numero
    print(f"{numero} x {i} = {resultado}")

mostrar_tabla(3)
mostrar_tabla(7)
mostrar_tabla(9)
