import random
password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passw = int(input("cuantos caracteres?"))
contraseña = ""
for i in range(passw):
    password += random.choice(password) 

print(password)

