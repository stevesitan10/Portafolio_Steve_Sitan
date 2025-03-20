#Ejercicio
#Crea una función llamada eliminar_especial que reciba una lista de números. La función debe comportarse de la siguiente manera:

#Si la lista tiene más de 5 elementos, debe eliminar el último elemento y devolver la lista modificada.
#Si la lista tiene exactamente 5 elementos, debe eliminar el elemento en la posición 2 y devolver la lista modificado.
#Si la lista tiene menos de 5 elementos debe devolver la lista sin modificar.
#Ejemplos:

#print(eliminar_elementos([1, 2, 3, 4]))  # Devuelve: (4, [1, 2, 3])
#print(eliminar_elementos([1, 2, 3, 4], 1))  # Devuelve: (2, [1, 3, 4])

def eliminar_especial(lista):
    largo_lista = len(lista)
    ultimo_elemento =  largo_lista - 1
    
    if largo_lista > 5:
        lista.pop()
        return lista
    elif largo_lista == 5: 
        lista.pop(2)
        return lista
    else: 
        return lista 

print(eliminar_especial([10, 20, 30, 40, 50, 60]))
print(eliminar_especial(["manzana", "pera", "uva", "naranja", "kiwi"]))
print(eliminar_especial([1, "dos", 3.0, "cuatro"]))
