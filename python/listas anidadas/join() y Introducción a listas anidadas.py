#Ejercicio
#Crea una función llamada mostrar_elementos que reciba una lista de compras organizada por categorías (una lista anidada) y muestre todos los elementos separados por puntos suspensivos (tres puntos), sin distinguir entre categorías.

#lista_compras = [
#    ["Manzanas", "Plátanos", "Uvas"],
#    ["Leche", "Yogur"],
#    ["Pan", "Cereales", "Galletas"]
#]
#mostrar_elementos(lista_compras)
# Debe imprimir: Manzanas...Plátanos...Uvas...Leche...Yogur...Pan...Cereales...Galletas

def mostrar_elementos(lista_compras):
    # Aplanar la lista anidada y unir los elementos con "..."
    print("...".join(item for categoria in lista_compras for item in categoria))
