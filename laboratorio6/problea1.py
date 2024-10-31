import random
import string

def generar_contraseña(longitud):
    if longitud < 8:
        print("La longitud mínima de la contraseña es de 8 caracteres.")
        return None
    
    # Caracteres disponibles para cada requisito
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiales = "!@#$%&*"

    # Garantizar que al menos uno de cada tipo esté en la contraseña
    contraseña = [
        random.choice(letras_mayusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiales)
    ]

    # Rellenar la longitud restante con una mezcla de todos los tipos de caracteres
    todos_caracteres = letras_mayusculas + letras_minusculas + numeros + caracteres_especiales
    while len(contraseña) < longitud:
        contraseña.append(random.choice(todos_caracteres))
    
    # Mezclar los caracteres para evitar patrones predecibles
    random.shuffle(contraseña)
    
    # Convertir la lista de caracteres en una cadena
    return ''.join(contraseña)

# Ejemplo de uso
longitud = 12
contraseña_generada = generar_contraseña(longitud)
print(f"Contraseña generada: {contraseña_generada}")
