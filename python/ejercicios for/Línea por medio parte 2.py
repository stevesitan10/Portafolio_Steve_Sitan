#Crea una función llamada lineas_verticales_alternadas que reciba dos números filas y columnas como parámetros y muestre en la consola un patrón de líneas verticales alternadas con asteriscos y espacios en blanco.

#Ejemplos:

#lineas_verticales_alternadas(3, 5)
#* * *
#* * *
#* * *

#lineas_verticales_alternadas(4, 4)
#* * 
#* * 
#* * 
#* * 
#La función no debe retornar valor alguno, utiliza print() para mostrar el patrón. 
#Asegúrate de que tu función funcione correctamente incluso para casos donde el número de filas o columnas sea 1.

def lineas_verticales_alternadas(filas, columnas):
    valor = ""
    for i in range(1, filas * 2 +1 ):
        if i % 2 == 0:
            valor = ""
            print(valor)
        else:
            for h in range(1,columnas + 1):
                if h % 2 == 0:
                    valor = valor + " "
                else:
                    valor = valor + "*"
            print(valor)

lineas_verticales_alternadas(4,5)
lineas_verticales_alternadas(2,3)
lineas_verticales_alternadas(1,6)
lineas_verticales_alternadas(5,1)

#Resultado
#* * *

#* * *

#* * *

#* * *

#* *

#* *

#* * * 

#*

#*

#*

#*

#*
        
