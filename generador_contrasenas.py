# Generador de contraseñas simple usando solo lo visto

def generar_contrasena(longitud):
    # Lista de caracteres posibles
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    contrasena = ""
    
    # Generar contraseña
    i = 0
    while i < longitud:
        # Elegir un carácter "aleatorio" simulando aleatoriedad con el índice
        indice = (i * 7 + 3) % len(caracteres)  # fórmula simple para variar el índice
        contrasena += caracteres[indice]
        i += 1
    
    return contrasena

def ejecutar():
    l = int(input("Longitud de la contraseña: "))
    print("Contraseña generada:", generar_contrasena(l))

ejecutar()
