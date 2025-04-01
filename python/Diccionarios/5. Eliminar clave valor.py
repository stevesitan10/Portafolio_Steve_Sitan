#Ejercicio
#Se está desarrollando un sistema de gestión de inventario para una tienda. Se tiene un diccionario que representa el inventario actual de productos y sus cantidades como se muestra a continuación:

#inventario = {
#    "manzanas": 50,
#    "plátanos": 30,
#    "naranjas": 40,
#    "peras": 25,
#    "uvas": 35
#}
#Tu tarea es crear una función llamada actualizar_inventario que realice lo siguiente:

#Si se le pasa un producto existente y una cantidad se debe editar la cantidad en el inventario.
#Si la cantidad pasada es 0 se debe eliminar el producto del inventario.
#La función debe recibir como argumentos un diccionario que representa el inventario, un string que representa el producto y un entero que representa la cantidad. La función debe retornar el inventario modificado.

#Ejemplo:

#inventario = {"manzanas": 50, "plátanos": 30, "naranjas": 40, "peras": 25, "uvas": 35}
#actualizar_inventario(inventario, "manzanas", 20) # {"manzanas": 20, "plátanos": 30, "naranjas": 40, "peras": 25, "uvas": 35}
#actualizar_inventario(inventario, "peras", 0) # {"manzanas": 20, "plátanos": 30, "naranjas": 40, "u

def actualizar_inventario(diccionario, item, valor):
    if item in diccionario:
        if valor == 0:
            diccionario.pop(item)  # Elimina el producto si la cantidad es 0
        else:
            diccionario[item] = valor  # Actualiza la cantidad si no es 0
    return diccionario

print(actualizar_inventario({'manzanas': 50, 'plátanos': 30, 'naranjas': 40, 'peras': 25, 'uvas': 35},'manzanas',20))
print(actualizar_inventario({'camisas': 20, 'pantalones': 15, 'zapatos': 10, 'sombreros': 5}, 'zapatos', 0))
