#Ejercicio
#Crea una función llamada mensajeOculto que reciba una lista y retorne un texto con el mensaje escondido utilizando solo la primera letra de cada elemento de la lista.

#Ejemplo:

#mesajeOculto(["Sol", "Elefante", "Casa", "Rana", "Estrella", "Tigre", "Oso"]) ## "SECRETO"
#Tip: Recuerda la función substring para obtener una subcadena de un string. Tip 2: De la misma forma que sumas números, puedes concatenar strings. Tip 3: Necesitas inicializar un string vacío para ir concatenando las letras.

  def mensajeOculto(lista):
  return " ".join(x[0:1] for x in lista)

print(mensajeOculto(["Gallina", "Abeja", "Tigre", "Oso"]))
print(mensajeOculto(["Música", "Isla", "Sol", "Tren", "Elefante", "Ratón", "Iguana","Oso"]))
print(mensajeOculto(["Luna", "Loro", "Avión", "Vaca", "Elefante"]))
