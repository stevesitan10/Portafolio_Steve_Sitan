## Importar la libreria pandas
````
import pandas as pd

````
## Importar el archivo csv
Las rutas en Windows usan la barra invertida (\), y Python la interpreta como un carácter de escape (por ejemplo, \n, \t, \u).

##🔧 Soluciones:
- ✅ Opción 1: Usa r antes de la cadena (raw string)
- ✅ Opción 2: Usa doble barra invertida \\
- ✅ Opción 3: Usa barras normales /
````
df = pd.read_csv(r"C:\Users\steve\OneDrive\Documentos\python\base_datos_2008.csv", nrows= 100000) 
````
 ## Ver las primeras 10 filas
````
df.head(10) #Nos da las primeras 5 filas
````
## Ver las ultimas 10 filas
````
df.tail() #Nos da las ultimas 5 filas
````
## reordena aleatoriamente todas las filas de un DataFrame de Pandas. 
````
df = df.sample(frac=1)`# frac es un argumento que especifica la fracción de filas que se devolverán en la muestra  frac=1 indica que se debe devolver el 100% de los datos, es decir, todas las filas
````
## Devolver las columnas de la tabla
````
df.columns
````
## Mostrar que tipo de variable es cada una 
````
df.dtypes
````


