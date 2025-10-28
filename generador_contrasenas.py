# generador_contrasenas.py

import random
import string

def generar_contrasena(longitud: int,
                       usar_minusculas=True,
                       usar_mayusculas=True,
                       usar_numeros=True,
                       usar_simbolos=True) -> str:
    """
    Genera una contraseña aleatoria de longitud 'longitud'.
    Puedes elegir qué tipos de caracteres incluir.
    """

    caracteres = ""

    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    # Si no se seleccionó ningún tipo de carácter
    if not caracteres:
        raise ValueError("Debes permitir al menos un tipo de caracteres.")

    # Seleccionar caracteres aleatorios
    return ''.join(random.choice(caracteres) for _ in range(longitud))


def ejecutar():
    print("\n=== Generador de Contraseñas ===")

    while True:
        try:
            longitud = int(input("Longitud de la contraseña: "))
            break
        except ValueError:
            print("Ingresa un número entero válido.")

    print("\nSelecciona qué incluir:")
    usar_minusculas = input("¿Minúsculas? (s/n): ").lower() == "s"
    usar_mayusculas = input("¿Mayúsculas? (s/n): ").lower() == "s"
    usar_numeros = input("¿Números? (s/n): ").lower() == "s"
    usar_simbolos = input("¿Símbolos? (s/n): ").lower() == "s"

    try:
        contrasena = generar_contrasena(longitud,
                                        usar_minusculas,
                                        usar_mayusculas,
                                        usar_numeros,
                                        usar_simbolos)
        print("\nContraseña generada:\n", contrasena)
    except ValueError as e:
        print("\nError:", e)


if __name__ == "__main__":
    ejecutar()
