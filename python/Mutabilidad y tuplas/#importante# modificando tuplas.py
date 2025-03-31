#Tuplas son inmutables
#No puedes modificar sus valores después de la creación.

#mi_tupla = (1, 2, 3)
#mi_tupla[0] = 100  # ❌ Error: TypeError
#✅ Solución si necesitas cambiar valores → Convertirla en lista.


#mi_tupla = (1, 2, 3)
#mi_lista = list(mi_tupla)  # Convertir a lista
#mi_lista[0] = 100  # Modificar
#mi_tupla = tuple(mi_lista)  # Convertir de nuevo a tupla
#print(mi_tupla)  # (100, 2, 3)


#Ejercicio
#Crea una función llamada aumentar_notas que reciba una tupla de calificaciones y le sume 1 punto a cada una de ellas. Tendrás que crear una nueva tupla con las calificaciones aumentadas ya que las tuplas son inmutables.

#Ejemplo de uso:

#calificaciones = (75, 45, 80, 65, 90)
#nuevas_calificaciones = aumentar_notas(calificaciones)
#print(nuevas_calificaciones) # Debe mostrar: (76, 46, 81, 66, 91)

def aumentar_notas(notas):
  notas_list = list(notas)
  return tuple(x + 1 for x in notas_list)

print(aumentar_notas((75, 45, 80, 65, 90)))
