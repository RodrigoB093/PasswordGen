import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Longitud de la contraseña:"))
contraseña = ""

for i in range(longitud):
    contraseña += caracteres[random.randint(0,71)]

print("Contraseña generada:", contraseña)