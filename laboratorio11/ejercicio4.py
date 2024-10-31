from collections import Counter

def contador_palabras(archivo):
    try:
        with open(archivo, 'r') as file:
            texto = file.read().lower().split()
            contador = Counter(texto)
            palabras_mas_frecuentes = contador.most_common(10)
            
            for palabra, frecuencia in palabras_mas_frecuentes:
                print(f"{palabra}: {frecuencia}")
    except Exception as e:
        print(f"Error: {e}")

# Uso del programa
archivo = "mi_archivo.txt"
contador_palabras(archivo)
