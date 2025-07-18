import random

def generar_contrasena(longitud, usar_mayus, usar_minus, usar_num, usar_simbolos):
    caracteres = ""
    if usar_mayus:
        caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if usar_minus:
        caracteres += "abcdefghijklmnopqrstuvwxyz"
    if usar_num:
        caracteres += "1234567890"
    if usar_simbolos:
        caracteres += "+-/*!&$#?=@"
    
    if caracteres == "":
        return "Error: Debes seleccionar al menos un tipo de carácter."

    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Pedir datos al usuario
longitud = int(input("Longitud de la contraseña: "))
usar_mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
usar_minus = input("¿Incluir minúsculas? (s/n): ").lower() == "s"
usar_num = input("¿Incluir números? (s/n): ").lower() == "s"
usar_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"

# Generar y mostrar contraseña
resultado = generar_contrasena(longitud, usar_mayus, usar_minus, usar_num, usar_simbolos)
print("Contraseña generada:", resultado)
