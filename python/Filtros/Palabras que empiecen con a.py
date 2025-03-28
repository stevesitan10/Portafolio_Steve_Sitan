#Ejercicio
#Crea una función llamada filtrar_palabras_con_a que reciba una lista de palabras y retorne una nueva lista que contenga solo las palabras que empiezan con la letra 'a' de la lista original.

#palabras = ["auto", "casa", "avión", "perro", "árbol", "gato"]
#resultado = filtrar_palabras_con_a(palabras)
#print(resultado)  # Debe mostrar: ["auto", "avión", "árbol"]

def filtrar_palabras_con_a(lista):
  return list(filter(lambda x: x.startswith("a"), lista))

print(filtrar_palabras_con_a(["amigo", "banana", "casa", "ala", "perro"]))
print(filtrar_palabras_con_a(["zapato", "árbol", "avión", "azul", "rojo", "amarillo"]))
