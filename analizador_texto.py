# analizador_texto.py

import re

def contar_palabras(texto: str) -> int:
    """Cuenta el número de palabras en el texto."""
    palabras = re.findall(r'\b\w+\b', texto, flags=re.UNICODE)
    return len(palabras)


def contar_frases(texto: str) -> int:
    """Cuenta frases separadas por ., ?, !"""
    frases = re.split(r'[.!?]+', texto)
    # eliminar frases vacías por espacios o saltos
    frases = [f.strip() for f in frases if f.strip()]
    return len(frases)


def contar_parrafos(texto: str) -> int:
    """Cuenta párrafos separados por doble salto de línea."""
    parrafos = texto.split("\n\n")
    parrafos = [p.strip() for p in parrafos if p.strip()]
    return len(parrafos)


def analizar_texto(texto: str) -> None:
    print("\n--- Resultados del análisis ---")
    print("Palabras:", contar_palabras(texto))
    print("Frases:", contar_frases(texto))
    print("Párrafos:", contar_parrafos(texto))


def ejecutar():
    print("\n=== Analizador de Texto ===")
    print("1) Escribir texto manualmente")
    print("2) Leer texto desde un archivo .txt")

    opcion = input("> Seleccione una opción (1 o 2): ").strip()

    if opcion == "1":
        print("\nEscribe o pega tu texto (finaliza con Enter dos veces):")
        lineas = []
        while True:
            linea = input()
            if linea == "":
                break
            lineas.append(linea)
        texto = "\n".join(lineas)

    elif opcion == "2":
        nombre = input("Nombre del archivo (ej: texto.txt): ").strip()
        try:
            with open(nombre, "r", encoding="utf-8") as f:
                texto = f.read()
        except FileNotFoundError:
            print("\nNo se encontró el archivo. Intenta nuevamente.")
            return
    else:
        print("\nOpción inválida.")
        return

    analizar_texto(texto)


if __name__ == "__main__":
    ejecutar()
