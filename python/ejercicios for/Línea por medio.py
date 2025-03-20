#Para determinar si una fila es par o impar, podemos utilizar el operador módulo (%).

#if fila % 2 == 0:
    # Fila par
#else:
    # Fila impar
#Ejercicio
#Crea una función llamada lineas_alternadas que reciba dos números filas y columnas como parámetros y muestre en la consola un patrón de líneas alternadas de asteriscos.

def lineas_alternadas(filas,columnas):
    valor = ""
    for i in range(1,filas +1):
        if i % 2 == 0: 
            valor = ""
        else: 
            for H in range(1,columnas + 1):
                valor = valor + "*"
        print(valor)

lineas_alternadas(4,6)
lineas_alternadas(5,2)
lineas_alternadas(1,3)
lineas_alternadas(2,1)

#******

#******

#**

#**

#**
#***
#*
