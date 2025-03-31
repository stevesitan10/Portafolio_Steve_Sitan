#Ejercicio
#Crea una función llamada encontrar_palabra que reciba una lista anidada de palabras y una palabra a buscar. La función debe retornar una tupla con la posición (índice de la sublista, índice dentro de la sublista) donde se encuentra la palabra. Si la palabra no está en la lista, la función debe retornar None.

#lista_palabras = [
#    ["gato", "perro", "ratón"],
#    ["manzana", "banana", "cereza"],
#   ["rojo", "verde", "azul"]
#]
#print(encontrar_palabra(lista_palabras, "banana"))  # Debe mostrar: (1, 1)
#print(encontrar_palabra(lista_palabras, "elefante"))  # Debe Mostrar: None
#Tip: Usa bucles anidados para recorrer la lista. El método enumerate() puede ser útil para obtener tanto el índice como el valor en cada iteración.

def encontrar_palabra(lista, palabra):
    for i,  sublista in enumerate(lista):
        for j,  item  in enumerate(sublista):
            if palabra == item:
                return (f"({i},{j})")
            
    return None
  
print(encontrar_palabra([["gato", "perro", "ratón"], ["manzana", "banana", "cereza"], ["rojo", "verde", "azul"]], "verde"))
print(encontrar_palabra([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]], "j"))
