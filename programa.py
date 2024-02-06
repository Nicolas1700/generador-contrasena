# Se inicia programa de genera contraseñas

import random

# Se definen el grupo de caracteres que van a usarse para generar las constraseña
LETRAS_MINUSCULAS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
LETRAS_MAYUSCULAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                     "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
NUMEROS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
CARACTERES_ESPECIALES = ["/", "*", "-", "+", "#", "$", "%"]
valores = [LETRAS_MAYUSCULAS, LETRAS_MINUSCULAS,
           NUMEROS, CARACTERES_ESPECIALES]

cantidad_caracteres = 16
contador = 0

contrasena = ""

while contador < cantidad_caracteres:
    columna = random.randint(0, (len(valores) - 1))
    caracter = valores[columna][random.randint(1, (len(valores[columna]) - 1))]
    contrasena += caracter
    contador += 1

print("La contrasena generada es:", contrasena)
