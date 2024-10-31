def fibonacci(n):
    """Calcula la serie de Fibonacci hasta el n-ésimo término."""
    serie = []
    a, b = 0, 1
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie

# Ejemplo de uso
n = 10
print(f"Serie de Fibonacci hasta el término {n}: {fibonacci(n)}")
