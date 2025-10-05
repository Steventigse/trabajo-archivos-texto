# cierre manual con close()
f = open("my_notes.txt", "a", encoding="utf-8")
try:
    f.write("Quinta nota: cierre manual con close().\n")
finally:
    f.close()
print("¿Archivo de escritura cerrado?", f.closed)

f = open("my_notes.txt", "r", encoding="utf-8")
try:
    for i, linea in enumerate(f, start=1):
        print(f"Línea {i}: {linea.strip()}")
finally:
    f.close()
print("¿Archivo de lectura cerrado?", f.closed)
