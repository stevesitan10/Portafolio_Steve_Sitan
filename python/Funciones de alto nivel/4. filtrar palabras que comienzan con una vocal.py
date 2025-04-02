palabras = ["alto", "bajo", "enorme", "pequeño", "mediano"]
vocales = 'aeiou'
resultado = list(filter(lambda palabra: palabra[0].lower() in vocales, palabras))
print(resultado)  # Imprime: ['alto', 'enorme']
