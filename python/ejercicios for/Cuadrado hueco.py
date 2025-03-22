#Ejercicio
#Crea una función llamada cuadrado_hueco que reciba un número n como parámetro y muestre en la consola un cuadrado hueco de asteriscos de lado n.

#Ejemplos:

#cuadrado_hueco(3)
#***
#* *
#***

#cuadrado_hueco(5)
#*****
#*   *
#*   *
#*   *
#*****
#La función no debe retornar valor alguno, utiliza print() para mostrar el patrón. Asegúrate de que tu función funcione correctamente incluso para cuadrados de lado 1 o 2.

def cuadrado_hueco(lados):
    filas = lados  * 2
    columna = lados
    for i in range(1, filas):
        valor = ""
        if i % 2 == 0:
            valor = ""
            print(valor)
        else: 
            if i == 1:
                for h in range(1,columna +1 ):
                    valor = valor + "*"
            elif i == ((columna*2)-1):
                for h in range(1,columna+1):
                    valor = valor + "*"
            else: 
                for j in range(1,columna+1):
                    if j == 1:
                        valor = valor + "*"
                    elif j == columna:
                        valor = valor + "*"
                    else: 
                        valor = valor + " "     
                                  
        print(valor)

cuadrado_hueco(4)
cuadrado_hueco(2)
cuadrado_hueco(6)
cuadrado_hueco(1)
