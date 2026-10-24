#27 Simulador de Lanzamiento de Dado
import random

lanzamiento = 0
contador = 0

while lanzamiento != 6:
    lanzamiento = random.randint(1, 6)
    contador += 1
    print(f"Lanzamiento {contador}: Obtuviste un {lanzamiento}")

print(f"\n¡Se obtuvo un 6 en {contador} lanzamiento(s)!")