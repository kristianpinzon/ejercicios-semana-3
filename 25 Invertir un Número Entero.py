#25 Invertir un Número Entero
numero = int(input("Ingrese un número entero: "))

es_negativo = numero < 0
temp = abs(numero)

numero_invertido = 0
while temp > 0:
    digito = temp % 10
    numero_invertido = (numero_invertido * 10) + digito
    temp //= 10

if es_negativo:
    numero_invertido = -numero_invertido

print(f"Número invertido: {numero_invertido}")