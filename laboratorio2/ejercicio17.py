cadena = input("Introduce una cadena: ")
prefijo = input("Introduce el prefijo: ")
sufijo = input("Introduce el sufijo: ")

empieza_con = cadena.startswith(prefijo)
termina_con = cadena.endswith(sufijo)

print(f"¿La cadena empieza con '{prefijo}'? {empieza_con}")
print(f"¿La cadena termina con '{sufijo}'? {termina_con}")
