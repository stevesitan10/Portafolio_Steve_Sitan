#Ejercicio
#Crea una función llamada dibujar_tabla que reciba un parámetro n y muestre en la consola una tabla de n x n con números consecutivos.

#Ejemplo de uso:

#dibujar_tabla(3)
# Debe mostrar:
#  1  2  3
#  4  5  6
#  7  8  9

#dibujar_tabla(4)
# Debe mostrar:
#  1  2  3  4
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16
#La función no debe retornar valor alguno, utiliza print() para mostrar la tabla. Asegúrate de que los números estén correctamente alineados en columnas. Tu función debe funcionar para cualquier valor de n mayor que 0.
def dibujar_tabla(numero):
    fila = numero
    columna= numero
    valor = 0 
    for i in range(1, numero +1):
        for h in range (1,columna  + 1):
            valor = valor + 1 
            print(f"{valor}", end=" ")
        print()

dibujar_tabla(5)
dibujar_tabla(2)
dibujar_tabla(1)
dibujar_tabla(7)
