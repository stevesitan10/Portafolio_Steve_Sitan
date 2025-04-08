````
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

df = pd.read_csv(r"C:\Users\steve\OneDrive\Documentos\python\base_datos_2008.csv", nrows = 1000000)

np.random.seed(0)
df = df[df["Origin"].isin(["HOU", "ATL", "IND"])]
df.sample(frac=1)
df = df[0:10000]

df["BigDelay"] = df["ArrDelay"] > 30
observador = pd.crosstab(index=df["BigDelay"],columns=df["Origin"], margins= True)
````

![image](https://github.com/user-attachments/assets/b92e93a1-4f60-4fe9-bd2a-86551db9c3fb)
````
test = chi2_contingency(observador)
test
````
![image](https://github.com/user-attachments/assets/ba97ff7d-1e03-4950-a437-af796ae160b0)

## Respuesta

![image](https://github.com/user-attachments/assets/5eb43d6f-5072-4eb4-9108-eeb4a4ffe637)
