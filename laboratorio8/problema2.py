def calculadora(numero1, numero2, operacion):
    try:
        numero1, numero2 = float(numero1), float(numero2)
        operaciones = {
            "suma": lambda x, y: x + y,
            "resta": lambda x, y: x - y,
            "multiplicacion": lambda x, y: x * y,
            "division": lambda x, y: x / y
        }
        if operacion not in operaciones:
            raise ValueError("Operación no válida. Usa: suma, resta, multiplicacion, division.")
        if operacion == "division" and numero2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        
        resultado = operaciones[operacion](numero1, numero2)
        return resultado
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None

# Solicitar datos al usuario
num1 = input("Introduce el primer número: ")
num2 = input("Introduce el segundo número: ")
op = input("Introduce la operación (suma, resta, multiplicacion, division): ")

resultado = calculadora(num1, num2, op)
if resultado is not None:
    print(f"El resultado de la operación es: {resultado}")
