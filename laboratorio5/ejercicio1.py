# Lista de edades
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a. Ordena la lista y encuentra la edad mínima y máxima
edades_ordenadas = sorted(edades)
edad_minima = edades_ordenadas[0]
edad_maxima = edades_ordenadas[-1]
print(f"Edad mínima: {edad_minima}")
print(f"Edad máxima: {edad_maxima}")

# b. Añade de nuevo la edad mínima y máxima a la lista
edades_ordenadas.append(edad_minima)
edades_ordenadas.append(edad_maxima)
print(f"Lista con edad mínima y máxima añadidas: {edades_ordenadas}")

# c. Encuentra la edad mediana
n = len(edades_ordenadas)
if n % 2 == 1:
    edad_mediana = edades_ordenadas[n // 2]
else:
    edad_mediana = (edades_ordenadas[n // 2 - 1] + edades_ordenadas[n // 2]) / 2
print(f"Edad mediana: {edad_mediana}")

# d. Encuentra la edad promedio
edad_promedio = sum(edades_ordenadas) / len(edades_ordenadas)
print(f"Edad promedio: {edad_promedio:.2f}")

# e. Encuentra el rango de las edades
rango_edades = edad_maxima - edad_minima
print(f"Rango de las edades: {rango_edades}")

# f. Compara el valor de (mínimo - promedio) y (máximo - promedio)
comparacion_min = abs(edad_minima - edad_promedio)
comparacion_max = abs(edad_maxima - edad_promedio)
print(f"Comparación: |{edad_minima} - {edad_promedio:.2f}| = {comparacion_min}, |{edad_maxima} - {edad_promedio:.2f}| = {comparacion_max}")
