# Creación y uso de módulos
Supongamos que tenemos un archivo llamado operaciones.py con las siguientes funciones:
````
# operaciones.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

````
Podemos usar este módulo en otro archivo de la siguiente manera:

````
# main.py
import operaciones # Importamos el módulo que acabamos de crear

print(operaciones.sumar(5, 3))  # Muestra: 8
print(operaciones.restar(10, 4))  # Muestra: 6

````
También podemos importar solo las funciones que necesitamos:

````
# main.py
from operaciones import sumar # Desde el módulo operaciones importa sumar

print(sumar(5, 3))  # Muestra: 8

````
Adicionalmente, podemos importar un módulo con un alias:
````
# main.py
import operaciones as ops # Importamos el módulo operaciones con el alias ops

print(ops.sumar(5, 3))  # Muestra: 8
````


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

# ¿Qué es lambda en Python?
Una función lambda en Python es una función anónima (sin nombre) que se define en una sola línea con la palabra clave lambda.

Sintaxis

```
lambda argumentos: expresión

```
![image](https://github.com/user-attachments/assets/4c0ffdf4-5fce-419b-bb55-903ecb969945)

# Ejemplos prácticos
# ✅ Usar lambda en map()

![image](https://github.com/user-attachments/assets/e8bcf859-8e73-4bc7-b17c-240dfcd959e6)

map() aplica la función lambda a cada elemento de la lista.

# ✅ Usar lambda en filter()

![image](https://github.com/user-attachments/assets/c2841336-4916-4997-9aaf-96de048f48a4)

filter() usa la función lambda para seleccionar los números pares.

# ✅ Ordenar con lambda en sorted()

![image](https://github.com/user-attachments/assets/f087373b-c933-4e46-b65e-45db922fa78b)

# Cuándo usar lambda
- ✅ Cuando necesitas una función corta y simple.
- ✅ Para pasar funciones a map(), filter(), sorted(), etc.
- ❌ No cuando la función tiene múltiples líneas o lógica compleja (usa def en su lugar).


