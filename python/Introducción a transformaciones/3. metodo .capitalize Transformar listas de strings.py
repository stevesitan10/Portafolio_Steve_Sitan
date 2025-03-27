#Capitalizando nombres en una lista
#En Python, podemos capitalizar un string (convertir su primera letra a mayúscula) usando el método capitalize(). Para aplicar esto a todos los elementos de una lista, necesitamos iterar sobre la lista y modificar cada elemento.
#Veamos un ejemplo de cómo capitalizar un solo nombre:

nombre = "ana"
nombre_capitalizado = nombre.capitalize()
print(nombre_capitalizado)  # Imprime: Ana

#Ejercicio
#Crea una función llamada capitalizar_nombres que reciba una lista de nombres y retorne una nueva lista con los nombres capitalizados.

#Ejemplo:

#nombres = ["ana", "luis", "jose", "rosa", "julio"]
#resultado = capitalizar_nombres(nombres)
#print(resultado)  # Debe imprimir: ['Ana', 'Luis', 'Jose', 'Rosa', 'Julio']

def capitalizar_nombres(lista):
  lista2 = list(map(lambda x: x.capitalize(), lista))
  return lista2

print(capitalizar_nombres(["maria", "carlos", "ana", "pedro"]))
print(capitalizar_nombres(["juan", "lucia", "pablo", "luisa", "josefina"]))
