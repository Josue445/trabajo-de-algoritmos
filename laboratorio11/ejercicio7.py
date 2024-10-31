def cifrar_archivo(archivo, desplazamiento):
    try:
        with open(archivo, 'r') as file:
            texto = file.read()
        
        texto_cifrado = ''.join(
            chr((ord(c) + desplazamiento - 97) % 26 + 97) if c.islower() else
            chr((ord(c) + desplazamiento - 65) % 26 + 65) if c.isupper() else c
            for c in texto
        )

        with open(f"{archivo}_cifrado.txt", 'w') as file:
            file.write(texto_cifrado)
        print("Archivo cifrado guardado.")
    except Exception as e:
        print(f"Error: {e}")

# Uso del programa
cifrar_archivo("mi_archivo.txt", 3)
