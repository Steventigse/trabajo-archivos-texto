# Paso 2: leer my_notes.txt línea por línea y mostrar en consola

print("Leyendo my_notes.txt...")
with open("my_notes.txt", "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, start=1):
        print(f"Línea {i}: {linea.strip()}")  # .strip() quita el salto de línea

# Al salir del 'with', el archivo se cierra automáticamente.
