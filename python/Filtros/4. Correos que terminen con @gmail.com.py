#Ejercicio
#Se tiene una lista con varios correos electrónicos. Crea una función llamada filtrar_correos_gmail que reciba una lista de correos electrónicos y retorne una nueva lista que contenga solo los correos que terminen con "@gmail.com".

#correos = ["usuario@gmail.com", "otro@hotmail.com", "alguien@gmail.com", "persona@yahoo.com"]
#resultado = filtrar_correos_gmail(correos)
#print(resultado)  # Debe mostrar: ["usuario@gmail.com", "alguien@gmail.com"]

def filtrar_correos_gmail(lista):
  return list(filter(lambda x: x.endswith("@gmail.com"), lista))

print(filtrar_correos_gmail(["juan@gmail.com", "maria@hotmail.com", "pedro@gmail.com", "ana@yahoo.com"]))
print(filtrar_correos_gmail(["empresa@outlook.com", "soporte@gmail.com", "info@company.com", "contacto@gmail.com"]))
