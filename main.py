cat > main.py << 'EOF'
from pathlib import Path
import argparse

FILE = Path("my_notes.txt")

def escribir():
    notas = [
        "Primera nota: repasar Python y Git.\n",
        "Segunda nota: terminar el proyecto de la clase.\n",
        "Tercera nota: subir cambios a GitHub.\n",
    ]
    with FILE.open("w", encoding="utf-8") as f:
        f.writelines(notas)
    print(f"✅ Escrito: {FILE.resolve()}")

def leer():
    if not FILE.exists():
        print("⚠️ No existe my_notes.txt. Ejecuta primero: python main.py --write")
        return
    with FILE.open("r", encoding="utf-8") as f:
        for i, linea in enumerate(f, 1):
            print(f"Línea {i}: {linea.strip()}")
    print("✅ Lectura terminada.")

def append(texto: str):
    with FILE.open("a", encoding="utf-8") as f:
        f.write(texto + "\n")
    print("✅ Línea agregada.")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Demo lectura/escritura de archivos de texto.")
    p.add_argument("--write", action="store_true", help="Crear y escribir notas")
    p.add_argument("--read", action="store_true", help="Leer línea por línea")
    p.add_argument("--append", type=str, help="Agregar una línea al final")
    args = p.parse_args()

    if args.write: escribir()
    if args.read: leer()
    if args.append: append(args.append)
    if not any([args.write, args.read, args.append]):
        p.print_help()
EOF
