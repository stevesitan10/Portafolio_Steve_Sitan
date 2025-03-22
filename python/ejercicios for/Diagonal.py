#Ejercicio
#Crea una función llamada diagonal_cuadrado que reciba un número n como parámetro y muestre en la consola la diagonal de un cuadrado de lado n.

#Ejemplos:

#diagonal_cuadrado(3)
#*  
# * 
#  *

#diagonal_cuadrado(5)
#*    
# *   
#  *  
#   * 
#    *
#La función no debe retornar valor alguno, utiliza print() para mostrar el patrón. Asegúrate de que tu función funcione correctamente incluso para casos donde el lado del cuadrado sea 1 o 2.

# Escribe tu código aquí

def diagonal_cuadrado(lado):
    fila = lado
    columna = lado
    valor = ""
    for i in range (1,fila* 2):
        if i % 2 == 0:
            print("")
        else: 
            if i == 1:
                valor = valor + "*"
            else:
                valor =  " " + valor
            print(valor)
            
diagonal_cuadrado(4)
diagonal_cuadrado(2)
diagonal_cuadrado(1)
diagonal_cuadrado(6)
