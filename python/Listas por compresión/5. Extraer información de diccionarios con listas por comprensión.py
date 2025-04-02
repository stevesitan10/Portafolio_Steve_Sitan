#Ejercicio
#Crea una función llamada obtener_titulos que tome una lista de diccionarios como parámetro, donde cada diccionario representa un libro con las claves 'titulo' y 'autor'. La función debe devolver una lista solamente con los títulos de los libros.

#Utiliza una lista por comprensión para realizar esta operación.

#Ejemplo de salida esperada:

#libros = [
#    {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry"},
#    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
#    {"titulo": "1984", "autor": "George Orwell"}
#]
#print(obtener_titulos(libros))  # Debe devolver: ['El principito', 'Cien años de soledad', 

def obtener_titulos(libros):
    return [libro["titulo"] for libro in libros]

print(obtener_titulos([{"titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}, {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}, {"titulo": "1984", "autor": "George Orwell"}]))
print(obtener_titulos( [{"titulo": "Don Quijote", "autor": "Miguel de Cervantes"}, {"titulo": "Hamlet", "autor": "William Shakespeare"}]))
print(obtener_titulos([{"titulo": "La Odisea", "autor": "Homero"}, {"titulo": "Orgullo y prejuicio", "autor": "Jane Austen"}, {"titulo": "Crimen y castigo", "autor": "Fyodor Dostoevsky"}]))
