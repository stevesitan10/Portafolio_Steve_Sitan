

# Uso de variables globales en funciones
En Python, las variables definidas fuera de cualquier función son globales y pueden ser accedidas desde dentro de las funciones. Sin embargo, para modificarlas dentro de una función, se debe declarar explícitamente que se está usando la variable global. Por ejemplo:

![image](https://github.com/user-attachments/assets/65b16923-0155-40b8-abca-15d329be42b0)

# Creación de variables locales sin global
En Python, cuando asignamos un valor a una variable dentro de una función sin usar la palabra clave global, se crea una nueva variable local, incluso si existe una variable global con el mismo nombre.

![image](https://github.com/user-attachments/assets/4eebadc8-cd79-4b51-af50-05a8c3a2716a)

En este ejemplo, modificar_x() crea una nueva variable local x en lugar de modificar la variable global x. Como resultado, la variable global x permanece sin cambios.

Nota: Este comportamiento puede ser confuso si no se tiene en cuenta, por lo que es importante ser consciente de ello al trabajar con variables dentro de funciones

# Uso de *args en funciones
En Python, *args permite a una función aceptar cualquier número de argumentos. Estos argumentos se empaquetan en una tupla dentro de la función.

Ejemplo:
```
def mostrar_argumentos(*args):
    print("Argumentos recibidos:")
    for arg in args:
        print(arg)

mostrar_argumentos("Hola", "Python")
print("---")
mostrar_argumentos("Uno", "Dos", "Tres", "Cuatro")
```


|Módulo|Versión|Descripción|
|--- |--- |--- |

-------


