import random 

variable = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
contraseña = int(input("dime los caracteres que quieres en la contraseña"))   
password = ""

for i in range(contraseña):
    password += random.choice(variable)

print(password)
