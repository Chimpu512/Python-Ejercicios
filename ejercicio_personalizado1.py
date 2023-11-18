#Crea un programa que genere contraseñas seguras.
#El programa debe permitir al usuario especificar la longitud de la contraseña y qué tipos de caracteres incluir 
#(letras mayúsculas, letras minúsculas, números y/o símbolos).

import random

longitud = int(input("Escribe el número de caracteres que quieres para tu contraseña: "))
chars = input("Escribe los caracteres que quieres que incluya tu contraseña: ")
password = ""

for _ in range(longitud):
    password += random.choice(chars)

print(password)

if longitud == 0:
    print("Número de caracteres inválido, ingresar nuevamente.")

def verificar_criterios():
    if any(letra.isupper() for letra in password):
        print("La contraseña contiene al menos una letra mayúscula.")
    else:
        print("La contraseña no contiene ninguna letra mayúscula. Por favor reingresa los datos")
    if any(numero.isdigit() for numero in password):
        print("La contraseña contiene al menos un número.")
    else:
        print("La contraseña no contiene ningún número. Por favor reingresa los datos")