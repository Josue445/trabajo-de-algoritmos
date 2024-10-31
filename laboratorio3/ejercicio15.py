telefono = input("Introduce un número de teléfono de 10 dígitos: ")

if len(telefono) == 10 and telefono.isdigit():
    telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"
    print(f"Número de teléfono formateado: {telefono_formateado}")
else:
    print("Número de teléfono no válido.")
