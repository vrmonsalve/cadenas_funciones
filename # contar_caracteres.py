# contar_caracteres.py 

def contar_vocales(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador


def contar_consonantes(texto):
    consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
    contador = 0
    for letra in texto:
        if letra in consonantes:
            contador += 1
    return contador


def contar_espacios(texto):
    return texto.count(" ")


def main():
    texto = input("Escribe un texto: ")
    vocales = contar_vocales(texto) 
    consonantes = contar_consonantes(texto)
    espacios = contar_espacios(texto)

    print("Vocales:", vocales)
    print("Consonantes:", consonantes)
    print("Espacios:", espacios)

if __name__ == "__main__":
    main()