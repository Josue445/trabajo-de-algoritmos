def procesador_texto(archivo):
    try:
        with open(archivo, 'a') as file:
            texto = input("Escribe el texto para añadir al archivo: ")
            file.write(texto + "\n")
            print("Texto añadido correctamente.")
    except Exception as e:
        print(f"Error: {e}")

# Uso del programa
archivo = "mi_archivo.txt"
procesador_texto(archivo)
