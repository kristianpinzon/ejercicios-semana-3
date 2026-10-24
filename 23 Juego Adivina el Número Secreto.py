#23 Juego "Adivina el Número Secreto"
import random

numero_secreto = random.randint(1, 10)
intentos = 0

print("¡Bienvenido al juego! He pensado un número entre 1 y 10.")

while True:
    intento = int(input("Adivina el número: "))
    intentos += 1
    
    if intento < numero_secreto:
        print("El número secreto es MAYOR.\n")
    elif intento > numero_secreto:
        print("El número secreto es MENOR.\n")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intento(s).")
        break