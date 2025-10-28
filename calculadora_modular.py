# calculadora_modular.py
"""
Calculadora modular — funciones reutilizables para operaciones básicas.

Funciones exportadas (públicas):
- sumar(a, b)
- restar(a, b)
- multiplicar(a, b)
- dividir(a, b)         # lanza ZeroDivisionError si b == 0
- modulo(a, b)          # lanza ZeroDivisionError si b == 0
- potencia(a, b)

Ejecutar el archivo directamente muestra un menú interactivo en consola.
"""

from typing import Union

Number = Union[int, float]


# --- Operaciones básicas (funciones puras) ---
def sumar(a: Number, b: Number) -> Number:
    """Devuelve a + b"""
    return a + b


def restar(a: Number, b: Number) -> Number:
    """Devuelve a - b"""
    return a - b


def multiplicar(a: Number, b: Number) -> Number:
    """Devuelve a * b"""
    return a * b


def dividir(a: Number, b: Number) -> Number:
    """Devuelve a / b. Lanza ZeroDivisionError si b == 0"""
    if b == 0:
        raise ZeroDivisionError("División por cero.")
    return a / b


def modulo(a: Number, b: Number) -> Number:
    """Devuelve a % b. Lanza ZeroDivisionError si b == 0"""
    if b == 0:
        raise ZeroDivisionError("Módulo por cero.")
    return a % b


def potencia(a: Number, b: Number) -> Number:
    """Devuelve a ** b"""
    return a ** b


# --- Utilidades para la interfaz/entrada ---
def pedir_numero(prompt: str = "Número: ") -> Number:
    """Pide un número al usuario (acepta enteros o flotantes). Reintenta hasta entrada válida."""
    while True:
        texto = input(prompt).strip()
        try:
            # Primero intento entero, si falla, float
            if texto == "":
                print("No ingresaste nada. Intenta de nuevo.")
                continue
            if "." not in texto and "e" not in texto and "E" not in texto:
                return int(texto)
            return float(texto)
        except ValueError:
            print("Entrada no válida. Escribe un número (ej. 3, 4.5, 1e-3).")


def mostrar_menu() -> None:
    print("""
Calculadora modular — elige una operación:
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Módulo
6) Potencia
7) Salir
""")


# --- Interacción principal (puede ejecutarse desde la línea de comandos) ---
def ejecutar_calculadora_interactiva() -> None:
    """Loop interactivo por consola."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-7): ").strip()
        if opcion == "7":
            print("Saliendo. ¡Hasta luego!")
            break

        if opcion not in {"1", "2", "3", "4", "5", "6"}:
            print("Opción no válida. Intenta de nuevo.")
            continue

        a = pedir_numero("Ingresa el primer número: ")
        b = pedir_numero("Ingresa el segundo número: ")

        try:
            if opcion == "1":
                resultado = sumar(a, b)
                operador = "+"
            elif opcion == "2":
                resultado = restar(a, b)
                operador = "-"
            elif opcion == "3":
                resultado = multiplicar(a, b)
                operador = "×"
            elif opcion == "4":
                resultado = dividir(a, b)
                operador = "÷"
            elif opcion == "5":
                resultado = modulo(a, b)
                operador = "%"
            elif opcion == "6":
                resultado = potencia(a, b)
                operador = "**"

            print(f"\n{a} {operador} {b} = {resultado}\n")

        except ZeroDivisionError as zde:
            print("Error:", zde)
        except Exception as e:
            print("Ocurrió un error inesperado:", e)


# --- Ejemplo de uso programático (import desde otro módulo) ---
def ejemplo_programatico():
    """Ejemplo de cómo usar las funciones desde otro código (no se ejecuta en import)."""
    x, y = 10, 3
    print("Ejemplo programático:")
    print("sumar:", sumar(x, y))
    print("restar:", restar(x, y))
    print("multiplicar:", multiplicar(x, y))
    print("dividir:", dividir(x, y))
    print("modulo:", modulo(x, y))
    print("potencia:", potencia(x, y))


if __name__ == "__main__":
    ejecutar_calculadora_interactiva()
