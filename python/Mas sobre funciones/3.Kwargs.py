# Ejercicio
#Crea una función llamada configurar_base_datos que simule la configuración de una conexión a una base de datos. La función debe tener valores predeterminados y permitir sobrescribirlos usando **kwargs. Los parámetros a manejar son:

#host (predeterminado: "localhost")
#puerto (predeterminado: 3306)
#usuario (predeterminado: "root")
#contraseña (predeterminado: "")
#nombre_bd (predeterminado: "mi_app")
#La función debe retornar un diccionario con la configuración final.

#Ejemplo:

#print(configurar_base_datos(puerto=5432, usuario="admin", nombre_bd="proyecto1"))
# Debe imprimir algo como:
# {"host": "localhost", "puerto": 5432, "usuario": "admin", "contraseña": "", "nombre_bd": "proyecto1"}


def configurar_base_datos(**kwargs):
  settings = {
    "host" : "localhost",
    "puerto" : 3306,
    "usuario" : "root",
    "contraseña": "",
    "nombre_bd": "mi_app"
  }
  
  settings.update(kwargs)
  return settings 

print(configurar_base_datos(puerto=5432, usuario="admin", nombre_bd="proyecto1"))
print(configurar_base_datos(host="192.168.1.1", contraseña="secreto"))
print(configurar_base_datos())
