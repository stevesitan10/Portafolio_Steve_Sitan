#Buscando información relacionada en múltiples listas
#A veces tenemos información relacionada almacenada en listas separadas, donde el índice es lo que relaciona los elementos entre las listas. Por ejemplo, podríamos tener una lista de productos y otra de sus respectivos stocks, donde el producto en la posición 0 de la lista de productos tiene su stock en la posición 0 de la lista de stocks.

#Ejemplo básico:

productos = ["manzana", "pera", "naranja"]
stocks = [50, 30, 75]

# El stock de "manzana" es 50
# El stock de "pera" es 30
# El stock de "naranja" es 75
#Para buscar información relacionada, necesitamos encontrar el índice del elemento en una lista y usar ese índice para acceder a la información en la otra lista.

Ejercicio
Crea una función llamada buscar_stock que reciba tres parámetros:

Una lista de nombres de productos
Una lista de stocks (en el mismo orden que los productos)
El nombre del producto a buscar
La función debe retornar el stock del producto buscado. Si el producto no se encuentra, debe retornar None.

Ejemplo de uso:

productos = ["manzana", "pera", "naranja", "uva"]
stocks = [50, 30, 75, 20]
print(buscar_stock(productos, stocks, "naranja"))  # Debe mostrar: 75
print(buscar_stock(productos, stocks, "plátano"))  # Debe mostrar: None
#Tip: Puedes usar un bucle con enumerate() para recorrer la lista de productos y obtener tanto el índice como el nombre del producto en cada iteración.

##solucion: 

def buscar_stock(productos, stocks, nombre):
  for i in range(len(productos)):
    if productos[i] == nombre:
      return stocks[i]
  return None


print(buscar_stock(["manzana", "pera", "naranja", "uva"],[50, 30, 75, 20],"naranja"))

print(buscar_stock(["laptop", "celular", "tablet", "smartwatch"],[10, 50, 25, 15],"impresora"))
