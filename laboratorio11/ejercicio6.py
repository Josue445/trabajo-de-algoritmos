import os
import shutil

def organizar_archivos(directorio):
    tipos = {
        "Imágenes": ['.jpg', '.jpeg', '.png', '.gif'],
        "Documentos": ['.txt', '.pdf', '.docx'],
        "Videos": ['.mp4', '.mov', '.avi'],
    }
    
    for archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, archivo)
        if os.path.isfile(ruta_archivo):
            for tipo, extensiones in tipos.items():
                if any(archivo.endswith(ext) for ext in extensiones):
                    carpeta_destino = os.path.join(directorio, tipo)
                    os.makedirs(carpeta_destino, exist_ok=True)
                    shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                    break

# Uso del programa
organizar_archivos("mi_directorio")
