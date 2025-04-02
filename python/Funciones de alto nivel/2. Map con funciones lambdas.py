#Ejercicio
#Crea una función lambda llamada corregir_nombre que reciba una lista de nombres en minúsculas y devuelva una lista con los nombres corregidos, es decir, con la primera letra en mayúscula y sin espacios al principio o al final.

#Ejemplo:

#corrige_nombres(["juan", " ana", "pedro  "])  # Debe devolver: ["Juan", "Ana", "Pedro"]

def corregir_nombre(lista):
    return list(map(lambda x: x.strip().capitalize() ,lista))

print(corregir_nombre(["juan", " ana", "pedro "]))
print(corregir_nombre([" maría ", "josé", " luis"]))
print(corregir_nombre(["CARLOS", "sofía ", " elena"]))
