Ejemplo básico:
cuadrados = [x**2 for x in range(5)]
print(cuadrados)  # [0, 1, 4, 9, 16]
x**2 → Es el nueva_valor, es decir, cada número de range(5) elevado al cuadrado.

for x in range(5) → Recorre los números 0, 1, 2, 3, 4.

Resultado: [0, 1, 4, 9, 16].

Ejemplo con if para filtrar datos:
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
x → Es el nueva_valor, el mismo número que se está iterando.

if x % 2 == 0 → Solo incluye números pares.

Resultado: [0, 2, 4, 6, 8].

Ejemplo aplicado a sum() con generador de expresiones:
suma_pares = sum(x for x in range(10) if x % 2 == 0)
print(suma_pares)  # 20
Aquí no se usa una lista explícita, sino un generador, lo que ahorra memoria.

x → Es el nueva_valor, los números pares de range(10).

if x % 2 == 0 → Filtra solo los pares.

sum(...) → Suma los valores generados.

Resultado: 0 + 2 + 4 + 6 + 8 = 20.

En resumen, nueva_valor es lo que defines como el valor generado/modificado en cada iteración. Puede ser el mismo elemento, una transformación o incluso una expresión matemática.
