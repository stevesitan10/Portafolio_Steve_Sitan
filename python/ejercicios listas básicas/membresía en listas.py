#Verificando membresía en listas
#Una membresía se refiere a la presencia de un elemento en la lista. En Python, el operador in nos permite verificar fácilmente si un elemento está presente en una lista. La sintaxis básica es:

#elemento in lista
#Esta expresión devuelve True si el elemento está en la lista y False si no lo está. Por ejemplo:

#frutas = ["manzana", "banana", "cereza", "dátil"]
#print("manzana" in frutas)  # True
#print("kiwi" in frutas)     # False

#Ejercicio
#Crea una función llamada miembro_en_dos que recibe 3 parámetros: arr1, arr2, y valor. La función debe retornar True si valor está presente en ambas listas arr1 y arr2, y False en caso contrario.

def miembro_en_dos(arr1,arr2, valor):
    a = valor in arr1 
    b = valor in arr2
    
    if a == True and b == True:
        return True 
    else:
        return False 
        

# Fin
arr1 = ["Nueva York", "Londres", "Tokio", "Sídney"]
arr2 = ["Londres", "París", "Tokio", "Berlín"]

print(miembro_en_dos(arr1, arr2, "Londres"))  
print(miembro_en_dos(arr1, arr2, "París"))   
print(miembro_en_dos(arr1, arr2, "Tokio"))  
