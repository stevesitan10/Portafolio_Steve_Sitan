# Demostración grafica de los Outliers

![image](https://github.com/user-attachments/assets/5dd923a4-9d62-4fe7-a544-2f35f406307d)

## Importar Librerias
````
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\steve\OneDrive\Documentos\python\base_datos_2008.csv", nrows = 100000)
````
## Extrar la columna de interes y eliminar los espacios vacios 
````
x = df["ArrDelay"].dropna()
````
## Con la formula inicila, calcular los percentiles Q1(Representa el 25%) y Q3(Representa el 75%)
![image](https://github.com/user-attachments/assets/88f8e1a1-1750-4c60-9f20-c9688d73e81f)

## Con la formula inicial, calcular el umbral superior e inferior

![image](https://github.com/user-attachments/assets/ebd1aae2-5312-4f80-b6ce-88af414d3776)

## Respuestas
Quiere decir que el umblar inferior esta por debajo de -46.5 y el umbralsuperior esta por encima de 328.5
![image](https://github.com/user-attachments/assets/b5961abc-327d-4528-b9a1-5911b268ad90)

## Si queremos saber el porcentaje de los datos que estan ya se por debajo o por encima:  
- Calculamos el porcentaje de los datos por encima del umbral superior que es *0.1139%* 
![image](https://github.com/user-attachments/assets/d7e30370-4a6d-4c92-82bf-7915c94db1ec)

- Calculamos el porcentaje de los datos por debajo del umbral inferior que es *0.07199%*
