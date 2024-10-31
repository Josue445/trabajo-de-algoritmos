from datetime import datetime

def registrar_evento(evento, archivo_log):
    try:
        with open(archivo_log, 'a') as file:
            tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{tiempo} - {evento}\n")
    except Exception as e:
        print(f"Error: {e}")

# Uso del programa
registrar_evento("Inicio de sesión exitoso", "registro_eventos.log")
