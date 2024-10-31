def buscador_palabras(archivo, palabra):
    try:
        with open(archivo, 'r') as file:
            for num_linea, linea in enumerate(file, start=1):
                if palabra in linea:
                    print(f"Línea {num_linea}: {linea.strip()}")
    except Exception as e:
        print(f"Error: {e}")

# Uso del programa
archivo = "mi_archivo.txt"
palabra = input("Introduce la palabra a buscar: ")
buscador_palabras(archivo, palabra)
