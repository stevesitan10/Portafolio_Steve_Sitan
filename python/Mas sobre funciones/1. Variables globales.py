#Modifica la función actualizar_total para que utilice la palabra clave global y actualice correctamente la variable global total.

contador = 0

def incrementar():
    global contador # Necesita la palabra clave global para modificar el contador 
    contador += 1
    print(contador)

incrementar()  # Muestra: 1
incrementar()  # Muestra: 2
print(contador) 
