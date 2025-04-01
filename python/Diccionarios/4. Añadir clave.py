#Ejercicio
#Crea una función llamada agregar_cuenta que reciba un lista con números enteros y devuelva un diccionario con la clave cuenta y el valor de la suma de los números de la lista. Si la lista está vacía, la función debe devolver un diccionario con la clave cuenta y el valor 0.

#Ejemplo

#agregar_cuenta([1, 2, 3, 4, 5]) # {'cuenta': 15}
#agregar_cuenta([]) # {'cuenta': 0}

def agregar_cuenta(lista):
  diccionario = {}
  diccionario["cuenta"] = sum(lista)
  return diccionario

print(agregar_cuenta([1, 2, 3, 4, 5]))
print(agregar_cuenta([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(agregar_cuenta([]))
