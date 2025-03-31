#Ejercicio
#Crea una función llamada modificar_calificaciones que reciba una tupla de calificaciones y realice las siguientes operaciones:

#Convertir la tupla a una lista.
#Si la primera calificación es menor a 70, aumentarla en 5 puntos.
#Si la última calificación es menor a 70, aumentarla en 5 puntos.
#Convertir la lista resultante de vuelta a una tupla y retornarla.
#Ejemplo de uso:

#calificaciones = (65, 80, 75, 90, 60)
#nuevas_calificaciones = modificar_calificaciones(calificaciones)
#print(nuevas_calificaciones)  # Debe mostrar: (70, 80, 75, 90, 65)
#Tip: Recuerda que puedes acceder al primer elemento de una lista con el índice 0 y al último con el índice -1.

def modificar_calificaciones(tupla):
  tupla_list = list(tupla)
  if tupla_list[0] < 70:
    tupla_list[0] = tupla_list[0] + 5
  if tupla_list[-1] < 70:
    tupla_list[-1] = tupla_list[-1] + 5
  return tuple(tupla_list)

print(modificar_calificaciones((65, 80, 75, 90, 60)))
print(modificar_calificaciones((75, 80, 85, 90, 95)))
