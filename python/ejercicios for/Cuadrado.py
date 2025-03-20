#Ejercicio
#Crea una función llamada cuadrado_relleno que reciba un número n como parámetro y muestre en la consola un cuadrado relleno de asteriscos de lado n.

#Ejemplos:

#cuadrado_relleno(3)
#***
#***
#***

#cuadrado_relleno(5)
#*****
#*****
#*****
#*****
#*****

def cuadro_relleno(Filas):
     
     for Fila_actual in range(1,Filas+1):
        asterisco = ''
        for  columnas in range(1,Filas+1):
            asterisco = asterisco + "*"
        print(asterisco)

  cuadro_relleno(5)

#*****
#*****
#*****
#*****
#*****

