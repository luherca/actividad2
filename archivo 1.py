import random

caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
cantidad=(int(input('¿cual es la cantidad de numeros que contendra tu contraseña?')))
contrasena=''
for i in range(cantidad):
    contrasena+=random.choice(caracteres)
print(contrasena)    