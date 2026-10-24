#29 Suma de los Dígitos de un Número
numero = int(input("Ingrese un número entero: "))
temp = abs(numero)
suma = 0

while temp > 0:
    suma += temp % 10
    temp //= 10

print(f"La suma de los dígitos de {numero} es: {suma}")