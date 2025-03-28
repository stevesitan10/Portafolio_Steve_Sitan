#Ejercicio
#Crea una función llamada filtrar_palabras_con_a_o_b que reciba una lista de palabras y retorne una nueva lista que contenga solo las palabras que empiezan con la letra 'a' o 'b' de la lista original.

#palabras = ["auto", "casa", "bote", "perro", "árbol", "banana"]
#resultado = filtrar_palabras_con_a_o_b(palabras)
#print(resultado)  # Debe mostrar: ["auto", "bote", "árbol", "banana"]

def filtrar_palabras_con_a_o_b(lista):
  return list(filter(lambda x: x.startswith("a") or x.startswith("b"), lista))

print(filtrar_palabras_con_a_o_b(["amigo", "casa", "bicicleta", "dedo", "elefante"]))
print(filtrar_palabras_con_a_o_b(["zapato", "árbol", "banana", "azul", "barco", "carro"]))
