# Listas de números
lista1 = list(range(1, 11))
lista2 = list(range(5, 16))
lista3 = list(range(10, 21))

# a. Convierte las listas en conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

# b. Encuentra el conjunto de todos los números presentes en las tres listas
conjunto_todos = conjunto1 & conjunto2 & conjunto3
print(f"Números presentes en las tres listas: {conjunto_todos}")

# c. Encuentra el conjunto de todos los números presentes en al menos una de las listas
conjunto_al_menos_una = conjunto1 | conjunto2 | conjunto3
print(f"Números presentes en al menos una lista: {conjunto_al_menos_una}")

# d. Encuentra el conjunto de todos los números presentes en la primera lista, pero no en la última
conjunto_unico_primera = conjunto1 - conjunto3
print(f"Números presentes en la primera lista pero no en la última: {conjunto_unico_primera}")

# e. Convierte los conjuntos obtenidos en tuplas y suma el primer y último elemento de cada tupla
tupla_todos = tuple(conjunto_todos)
tupla_al_menos_una = tuple(conjunto_al_menos_una)
tupla_unico_primera = tuple(conjunto_unico_primera)

print(f"Suma del primer y último elemento de tupla_todos: {tupla_todos[0] + tupla_todos[-1]}")
print(f"Suma del primer y último elemento de tupla_al_menos_una: {tupla_al_menos_una[0] + tupla_al_menos_una[-1]}")
print(f"Suma del primer y último elemento de tupla_unico_primera: {tupla_unico_primera[0] + tupla_unico_primera[-1]}")
