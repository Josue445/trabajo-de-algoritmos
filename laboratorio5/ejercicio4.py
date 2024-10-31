# Listas de tuplas
l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]
l2 = [("one", 1), ("two", 2), ("six", 6)]

# a. Crear conjuntos a partir de estas listas
s1 = set(l1)
s2 = set(l2)

# b. Encontrar los elementos que son comunes a s1 y s2
s3 = s1 & s2
print(f"Elementos comunes a s1 y s2: {s3}")

# c. Encontrar los elementos que son únicos para s1 y s2
s4 = s1 ^ s2
print(f"Elementos únicos para s1 y s2: {s4}")

# d. Crear una nueva lista l3 que contenga los elementos de s3 y s4 ordenados por el número entero de cada tupla
l3 = list(s3 | s4)  # Unión de s3 y s4
l3_ordenada = sorted(l3, key=lambda x: x[1])  # Ordenar por el número entero en cada tupla
print(f"Lista ordenada por número entero: {l3_ordenada}")
