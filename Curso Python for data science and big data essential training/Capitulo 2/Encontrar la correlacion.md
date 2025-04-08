
## 🟩 Paso 1:
````
df_numeric = df.select_dtypes(include=["number"])
````

🔍 ¿Qué hace?
- Filtra solo las columnas numéricas del DataFrame df.
- select_dtypes(include=["number"]) selecciona únicamente las columnas cuyo tipo de datos sea numérico (int, float).

![image](https://github.com/user-attachments/assets/c40e1bf6-d91c-4f32-a6f3-3623c7f8d3ca)

## 🟨 Paso 2:
````
corr = round(df_numeric.corr(), 3)
````

🔍 ¿Qué hace?
- Calcula la matriz de correlación de Pearson entre todas las columnas numéricas.
- .corr() evalúa la relación lineal entre variables (valores entre -1 y 1).
- round(..., 3) redondea cada valor a 3 decimales para una mejor visualización.

![image](https://github.com/user-attachments/assets/a0b47309-b18f-48da-ae6b-e8a287f6ecf8)

## 🟦 Paso 3:
````
corr.style.background_gradient(cmap='coolwarm')
````

🔍 ¿Qué hace?
- Le aplica un degradado de colores a la tabla de correlación para facilitar su lectura.
- cmap='coolwarm' es el nombre del mapa de colores (colores fríos para correlaciones negativas y cálidos para positivas).
- El color más oscuro indica correlaciones más fuertes (cercanas a ±1).
- Puedes cambiar el estilo visual usando otros cmap como 'viridis', 'Blues', 'RdYlGn', etc.

 ## 🧪 Resultado final:

 ![image](https://github.com/user-attachments/assets/d16c6049-0a71-4427-9792-1398dac0f771)

## 🎯 ¿Qué es la correlación?
La correlación de Pearson mide la fuerza y dirección de la relación lineal entre dos variables numéricas.

## 🧪 Ejemplo de matriz de correlación:

![image](https://github.com/user-attachments/assets/c620b633-a66b-4312-98eb-aaef31afad09)

## 🔍 Interpretación:

- ArrDelay vs DepDelay = 0.75 → Fuerte correlación positiva: si hay un retraso en la salida, es muy probable que también haya retraso en la llegada.
- Diagonal siempre es 1.0, porque es la correlación de una variable consigo misma.

## ✅ ¿Para qué sirve interpretar esto?
- Entender relaciones entre variables (por ejemplo, saber si una causa la otra).
- Reducir variables redundantes (dos variables muy correlacionadas pueden ser redundantes en modelos de machine learning).
- Detectar patrones (por ejemplo, si hay retrasos en ciertos días o con ciertas aerolíneas).
