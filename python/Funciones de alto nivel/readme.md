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
