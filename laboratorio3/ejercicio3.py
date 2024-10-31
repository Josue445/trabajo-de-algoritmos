notas = input("Introduce las notas separadas por comas: ")
notas_lista = [float(nota) for nota in notas.split(",")]
promedio = sum(notas_lista) / len(notas_lista)
print(f"El promedio de las notas es {promedio:.2f}")
