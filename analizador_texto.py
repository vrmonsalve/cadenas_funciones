# Analizador de texto simple
def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)
def contar_frases(texto):
    frases = []
    frase = ""
    for c in texto:
        frase += c
        if c in ".!?":
            if frase.strip():
                frases.append(frase.strip())
            frase = ""
    if frase.strip():
        frases.append(frase.strip())
    return len(frases)
def contar_parrafos(texto):
    parrafos = texto.split("\n\n")
    parrafos = [p for p in parrafos if p.strip()]
    return len(parrafos)
def analizar_texto(texto):
    print("\n--- Resultados del análisis ---")
    print("Palabras:", contar_palabras(texto))
    print("Frases:", contar_frases(texto))
    print("Párrafos:", contar_parrafos(texto))
def ejecutar():
    print("=== Analizador de Texto ===")
    texto = input("Escribe tu texto: ")
    analizar_texto(texto)
ejecutar()
