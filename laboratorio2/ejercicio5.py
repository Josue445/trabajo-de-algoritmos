try:
    valor = int(float('9.8'))
except ValueError:
    valor = None
print(f"¿Es int('9.8') igual a 10? {valor == 10}")
