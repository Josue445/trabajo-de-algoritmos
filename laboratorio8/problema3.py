import random
import string

def generador_contraseña(longitud, mayusculas=True, minusculas=True, numeros=True, especiales=True):
    try:
        longitud = int(longitud)
        if longitud < 1:
            raise ValueError("La longitud debe ser un número positivo.")
        
        # Definir conjuntos de caracteres
        conjuntos = {
            'mayusculas': string.ascii_uppercase if mayusculas else '',
            'minusculas': string.ascii_lowercase if minusculas else '',
            'numeros': string.digits if numeros else '',
            'especiales': "!@#$%&*" if especiales else ''
        }
        
        # Combinar todos los caracteres válidos
        caracteres_validos = ''.join(conjuntos.values())
        if not caracteres_validos:
            raise ValueError("Debes seleccionar al menos un tipo de carácter.")
        
        # Generar la contraseña aleatoria
        contraseña = ''.join(random.choice(caracteres_validos) for _ in range(longitud))
        return contraseña
    
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Solicitar datos al usuario
longitud = input("Introduce la longitud de la contraseña: ")
usar_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
usar_minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
usar_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
usar_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

contraseña = generador_contraseña(longitud, usar_mayusculas, usar_minusculas, usar_numeros, usar_especiales)
if contraseña:
    print(f"Contraseña generada: {contraseña}")
