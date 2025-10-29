# Calculadora modular simple
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división entre 0"
def ejecutar():
    while True:
        print("\nOpciones: sumar, restar, multiplicar, dividir, salir")
        op = input("Elige operación: ").lower()
        if op == "salir":
            break
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        if op == "sumar":
            print("Resultado:", sumar(a, b))
        elif op == "restar":
            print("Resultado:", restar(a, b))
        elif op == "multiplicar":
            print("Resultado:", multiplicar(a, b))
        elif op == "dividir":
            print("Resultado:", dividir(a, b))
        else:
            print("Opción no válida")
ejecutar()
