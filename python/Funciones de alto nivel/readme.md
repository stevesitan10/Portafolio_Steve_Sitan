# peración con map

Cuándo NO usar paréntesis ()
Cuando pasas una referencia a una función (sin ejecutarla)

En map(), filter(), sorted(), etc., se pasa una referencia de función sin paréntesis.

```
lista = ["ANA", "juan", "MaRia"]
nombres_formateados = list(map(str.capitalize, lista))  # Sin paréntesis en str.capitalize
print(nombres_formateados)
```
Si escribieras str.capitalize(), Python intentaría ejecutar el método sin un argumento, lo que daría error.

Cuando asignas una función a una variable sin ejecutarla

```
def cuadrado(x):
    return x ** 2

funcion = cuadrado  # Se asigna la referencia, no se ejecuta
print(funcion(5))   # Ahora sí se ejecuta
```
# Metodo Reduce()
El método reduce() en Python se encuentra en el módulo functools y se usa para reducir una secuencia a un solo valor aplicando una función acumulativa.

Sintaxis de reduce()
```
from functools import reduce

reduce(funcion, iterable[, valor_inicial])
```

funcion: Una función que toma dos argumentos y devuelve un solo valor.
````

iterable: La secuencia (lista, tupla, etc.) sobre la que se aplica la función.

valor_inicial (opcional): Un valor inicial para la acumulación.

````

![image](https://github.com/user-attachments/assets/9c97e731-3409-4d38-8e3b-bef67169c156)


![image](https://github.com/user-attachments/assets/e906dc7b-ef37-4ce1-b5e7-c59f1966fb22)
