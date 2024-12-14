import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Longitud de la contraseña:"))
contrasena = ""

for i in range(longitud):
    contrasena += caracteres[random.randint(0,71)]

print("Contraseña generada:", contrasena)
