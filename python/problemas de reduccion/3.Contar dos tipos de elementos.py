Si queres comparar dos cadenas sin importar si son mayúsculas o minúsculas, puedes convertir ambas cadenas a minúsculas antes de hacer la comparación. Por ejemplo:

nombre = "Camila"
if nombre.lower() == "camila":
  contador += 1

Ejercicio
Crea una función llamada contar_camila que reciba una lista de nombres y retorne la cantidad de veces que aparece el nombre "Camila" en la lista. La función debe ser sensible a mayúsculas y minúsculas, es decir, solo debe contar las ocurrencias exactas de "Camila".

Ejemplo:

print(contar_camila(["Ana", "Camila", "Carlos", "camila", "Camila"]))  # 2
print(contar_camila(["Juan", "Pedro", "Camila", "María", "Camila", "Luis"]))  # 2
Tip: Recuerda que puedes usar la comparación directa de cadenas en Python, por ejemplo: if nombre == "Camila".

## solucion 

def contar_camila(lista):
  conteo = 0
  for nombre in lista:
    if nombre == "Camila":
      conteo += 1
  return conteo
      
