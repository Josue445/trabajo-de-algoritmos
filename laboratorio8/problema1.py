def convertir_temperatura(temperatura, unidad):
    try:
        temperatura = float(temperatura)
        if unidad.upper() == 'C':
            # Convertir de Celsius a Fahrenheit
            return (temperatura * 9/5) + 32, "F"
        elif unidad.upper() == 'F':
            # Convertir de Fahrenheit a Celsius
            return (temperatura - 32) * 5/9, "C"
        else:
            raise ValueError("Unidad inválida. Usa 'C' para Celsius o 'F' para Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Solicitar datos al usuario
temp = input("Introduce la temperatura: ")
unidad = input("Introduce la unidad (C o F): ")

resultado = convertir_temperatura(temp, unidad)
if resultado:
    print(f"La temperatura convertida es: {resultado[0]:.2f}°{resultado[1]}")
