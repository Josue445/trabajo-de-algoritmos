def es_primo(n):
    """Determina si un número n es primo."""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primos_menores_que(n):
    """Encuentra todos los números primos menores que n."""
    return [num for num in range(2, n) if es_primo(num)]

n = 10
print(f"Números primos menores que {n}: {primos_menores_que(n)}")
