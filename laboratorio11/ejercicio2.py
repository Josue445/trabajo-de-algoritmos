import csv

def analizador_datos(archivo_csv):
    datos = []
    try:
        with open(archivo_csv, 'r') as file:
            lector = csv.reader(file)
            next(lector)  # Saltar encabezado si existe
            for fila in lector:
                datos.append(float(fila[0]))  # Suponiendo que el dato está en la primera columna
        
        media = sum(datos) / len(datos)
        maximo = max(datos)
        minimo = min(datos)

        print(f"Media: {media:.2f}, Máximo: {maximo}, Mínimo: {minimo}")
    except Exception as e:
        print(f"Error: {e}")

# Uso del programa
archivo_csv = "datos.csv"
analizador_datos(archivo_csv)
