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
                return in
