import csv

def generar_informe(archivo_csv, archivo_html):
    try:
        with open(archivo_csv, 'r') as file:
            lector = csv.reader(file)
            encabezados = next(lector)
            filas = [fila for fila in lector]

        with open(archivo_html, 'w') as file:
            file.write("<html><body><table border='1'>\n")
            file.write("<tr>" + "".join(f"<th>{encabezado}</th>" for encabezado in encabezados) + "</tr>\n")
            for fila in filas:
                file.write("<tr>" + "".join(f"<td>{dato}</td>" for dato in fila) + "</tr>\n")
            file.write("</table></body></html>")
        print(f"Informe HTML generado en {archivo_html}.")
    except Exception as e:
        print(f"Error: {e}")

# Uso del programa
generar_informe("datos.csv", "informe.html")
