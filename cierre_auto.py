# cierre automático con with
with open("my_notes.txt", "a", encoding="utf-8") as f:
    f.write("Cuarta nota: practicar lectura y cierre.\n")

with open("my_notes.txt", "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, start=1):
        print(f"Línea {i}: {linea.strip()}")
