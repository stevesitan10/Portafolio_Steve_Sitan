

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


# Kwargs
Ideas clave
- kwargs es abreviatura de "keyword arguments" (argumentos de palabra clave).
- kwargs permite pasar un número variable de argumentos de palabra clave a una función.
- Es similar a *args, pero en lugar de una tupla, kwargs crea un diccionario.
- Es comúnmente utilizado para funciones que aceptan muchos argumentos opcionales como por ejemplo funciones para crear configuraciones.

## Ejemplo de uso de **kwargs
Veamos un ejemplo sencillo de cómo usar **kwargs en una función:

```
def funcion(**kwargs):
    print(kwargs) 

funcion(a=1, b=2, c=3) # Muestra: {'a': 1, 'b': 2, 'c': 3}
funcion(nombre="Juan", edad=30) # Muestra: {'nombre': 'Juan', 'edad': 30}

````

# Uso de kwargs para configuraciones
Un ejemplo común de uso de **kwargs es para configuraciones. Podemos tener una función que configure una aplicación con valores predeterminados y permita sobrescribirlos con argumentos de palabra clave. Por ejemplo:

![image](https://github.com/user-attachments/assets/71cb7444-fe2f-4d82-903d-9a09962f22de)

