#Ejercicio
#Crea una función llamada media_piramide_izquierda que reciba un número altura como parámetro y muestre en la consola la parte izquierda de una pirámide con esa altura.

#Ejemplos:

#media_piramide_izquierda(3)
#  *
# **
#***

#media_piramide_izquierda(5)
#    *
#   **
#  ***
# ****
#*****
#La función no debe retornar valor alguno, utiliza print() para mostrar el patrón. Asegúrate de que tu función funcione correctamente incluso para casos donde la altura sea 1.

def media_piramide_izquierda(lado):
    fila = lado
    columna = lado
    valor = ""
    espacio = " "
    for i in range (1,fila +1):
        x = (columna-i)
        y = espacio*x
        z = i * "*"    
        print(y+z)



# Fin
media_piramide_izquierda(4)
media_piramide_izquierda(2)
media_piramide_izquierda(1)
media_piramide_izquierda(6)
