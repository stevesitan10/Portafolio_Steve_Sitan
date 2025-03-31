_____________________________________________________________
metodos utilizados:

🔹 isinstance(varieble, tipo). devuelde TRUE or FALSE

print(isinstance(5, int))  # Muestra: True
print(isinstance([1, 2], list))  # Muestra: True
_____________________________________________________________

🔹El método enumerate() en Python se usa para recorrer una secuencia (como listas, tuplas o cadenas) y obtener tanto el índice como el valor de cada elemento en un bucle.

sintaxis= enumerate(iterable, start=0)
_______________________________________________________________
🔹 ¿Qué son las sublistas en Python?
Una sublista es simplemente una lista dentro de otra lista. Se usa cuando queremos organizar datos en grupos dentro de una estructura más grande.

Ejemplo:

![image](https://github.com/user-attachments/assets/961b39e7-71a2-460e-8c60-351299eb5931)

Aquí tenemos una lista con 3 sublistas, cada una conteniendo elementos de una categoría.

🔹 ¿Cómo recorrer sublistas?
Para recorrer una lista anidada (con sublistas), usamos dos bucles for:

1. El primer for recorre cada sublista.

2. El segundo for recorre los elementos dentro de cada sublista.

![image](https://github.com/user-attachments/assets/cf1f3953-7aae-4aae-a28e-48c76b0c309b)

🔹 Salida:

Manzanas
Plátanos
Uvas
Leche
Yogur
Pan
Cereales
Galletas

🔹 Otra forma: Usando sum() con listas anidadas
Podemos convertir la lista de listas en una sola lista usando sum(lista, []):

![image](https://github.com/user-attachments/assets/9cae7be2-9c1b-43b4-9c69-644f5cb5dbe4)


🔹 Usando una comprensión de listas
Otra manera eficiente de recorrer y extraer elementos de una lista anidada:

![image](https://github.com/user-attachments/assets/87f11fb8-2a3a-4a43-9d66-c26f34aa8cab)


ejemplo de uso con listas de compresion 
![image](https://github.com/user-attachments/assets/9dc9823b-113c-41aa-a0b5-a063f3440622)


