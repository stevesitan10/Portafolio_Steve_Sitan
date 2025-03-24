#Ejercicio
#Modifica la siguiente función para que se muestren los datos de una lista en el siguiente formato: "El valor en la posición 0 es Galleta", utilizando un bucle while.

def mostrar_dato_e_indice(datos):
    i = 0
    while i < len(datos):
        print(f" El valor en la posición {i} es {datos[i]}")
        i += 1
# Fin
mostrar_dato_e_indice(["Galleta", "Chocolate", "Caramelo"])

 El valor en la posición 0 es Galleta
 El valor en la posición 1 es Chocolate
 El valor en la posición 2 es Caramelo
