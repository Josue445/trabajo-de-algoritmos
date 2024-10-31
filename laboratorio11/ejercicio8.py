import zipfile

def comprimir_archivos(archivos, nombre_zip):
    try:
        with zipfile.ZipFile(nombre_zip, 'w') as zipf:
            for archivo in archivos:
                zipf.write(archivo)
        print(f"Archivos comprimidos en {nombre_zip}")
    except Exception as e:
        print(f"Error: {e}")

# Uso del programa
comprimir_archivos(["mi_archivo.txt", "otro_archivo.txt"], "archivos.zip")
