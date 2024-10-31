def copiar_archivo(origen, destino):
    try:
        with open(origen, 'r') as archivo_origen:
            with open(destino, 'w') as archivo_destino:
                archivo_destino.write(archivo_origen.read())
        print(f"Contenido copiado de {origen} a {destino}.")
    except Exception as e:
        print(f"Error: {e}")

# Uso del programa
copiar_archivo("mi_archivo.txt", "copia_archivo.txt")
