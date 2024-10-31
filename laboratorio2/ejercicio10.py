cadena = input("Introduce una cadena: ")
vocales = 'aeiouAEIOU'
contador = sum(1 for char in cadena if char in vocales)
print(f"Número de vocales: {contador}")
