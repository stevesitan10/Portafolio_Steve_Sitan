##Crea una función llamada limpiar_y_agregar que reciba una lista y un parámetro llamado nombre. La función debe remover 
##los espacios vacíos al inicio y al final del nombre y luego 
##agregar el nombre al final de la lista.
##Finalmente, la función debe retornar la lista.

## Ejemplo: limpiar_y_agregar(["Juan", "Pedro", "Ana", "Luis"], "  Maria  ")  # ["Juan", "Pedro", "Ana", "Luis", "Maria"]

## Solucion 
def agregar_si (lista, nombre):
    largo = len(lista)
    if largo < 5:
        lista.append(nombre)
        return lista
    else: 
        return lista

print(limpiar_y_agregar(["uno", "dos", "tres", "cuatro"], "       cinco"))
print(limpiar_y_agregar(["Camilo", "Ignacio", "Constanza"], "      Juana     "))
print(limpiar_y_agregar(["perro", "gato", "pájaro", "pez"], "    cabra   "))


