# palindromo.py

def es_palindromo(texto):
    # Convertimos a minúsculas y quitamos espacios
    texto = texto.lower().replace(" ", "")
    # Comparamos el texto original con su inverso
    return texto == texto[::-1]

def main():
    cadena = input("Escribe una palabra o frase: ")
    if es_palindromo(cadena):
        print("Es un palíndromo ✅")
    else:
        print("No es un palíndromo ❌")

if __name__ == "__main__":
    main()
