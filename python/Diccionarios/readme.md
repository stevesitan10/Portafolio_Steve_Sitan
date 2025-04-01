_____________________________________________________________________________________________________
❄️ Es posible utilizar el método get() para obtener el valor asociado a una llave en un diccionario.

print(estudiante.get("nombre")) # Juan

❄️ La ventaja de get() es que si la llave no existe, no se generará un error, sino que se devolverá None.

print(estudiante.get("país")) # None
O incluso podemos definir un valor por defecto si la llave no existe.

print(estudiante.get("llave que no existe", "Valor por defecto")) # Valor por defecto
