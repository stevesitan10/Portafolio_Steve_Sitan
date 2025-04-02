#Ejercicio
#Completa la función concatenar_strings para que acepte cualquier número de strings como argumentos, los concatene con un espacio entre cada uno y luego los retorne.

#def concatenar_strings(*args):
    # Escribe tu código aquí



    # Fin
#    pass

#print(concatenar_strings("Hola", "mundo")) 
#print(concatenar_strings("Python", "es", "genial")) 

def concatenar_strings(*args):
  return " ".join(x for x in args)

print(concatenar_strings("Hola", "mundo")) 
print(concatenar_strings("Python", "es", "genial")) 
