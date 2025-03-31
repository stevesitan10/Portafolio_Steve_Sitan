#Contar elementos internos
#Ideas clave
#Las listas anidadas pueden representar estructuras de datos jerárquicas o agrupadas.
#No todas las sublistas en una lista anidada necesitan tener la misma longitud.
#Las listas anidadas son útiles para organizar datos relacionados en grupos.
#Con len podemos obtener la longitud de una lista.

def contar_por_categoria(lista):
    lista_conteo = []
    conteo = 0
    for sublista in lista:
        conteo = 0
        for item  in sublista:
            conteo = conteo + 1
        lista_conteo.append(conteo)        
    return lista_conteo 

print(contar_por_categoria([["Tomates", "Lechuga", "Pepinos"], ["Pollo", "Pescado"], ["Arroz", "Pasta"]]))
print(contar_por_categoria([["Manzanas", "Peras"], ["Leche"], ["Pan", "Tortillas", "Croissants", "Bagels"]]))
