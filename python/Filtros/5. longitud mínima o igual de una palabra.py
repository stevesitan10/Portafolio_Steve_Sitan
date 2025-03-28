#Ejercicio
#Se tiene una lista con datos que deberían tener 8 bits, es decir, 8 caracteres en donde cada caracter puede ser 0 o 1. Crea una función llamada filtrar_datos_errados que reciba la lista de datos y retorne una nueva lista únicamente con las cadenas que tienen exactamente 8 caracteres.

#datos = ["00010000", "00000001", "100000000", "1100000010", "00000000", "00000001", "00000000", "100000010"]
#datos_filtrados = filtrar_datos_errados(datos)
#print(datos_filtrados)  # Debe mostrar: ["00010000", "00000001", "00000000", "00000001", "00000000"]
#Tip: Puedes usar la función len() para obtener la longitud de una cadena. Por ejemplo, len("00000000") devuelve 8.

def filtrar_datos_errados(lista):
  return list(filter(lambda x: len(x) == 8, lista))

print(filtrar_datos_errados(["00010000", "00000001", "100000000", "1100000010", "00000000", "00000001", "00000000", "100000010"]))
print(filtrar_datos_errados(["1010101", "11111111", "000", "00000000", "1111111111", "01010101"]))
