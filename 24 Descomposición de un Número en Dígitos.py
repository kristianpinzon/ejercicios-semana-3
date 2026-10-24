#24 Descomposición de un Número en Dígitos
numero = int(input("Ingrese un número entero positivo: "))

if numero <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    temp = numero
    print(f"Dígitos de {numero} comenzando por las unidades:")
    while temp > 0:
        digito = temp % 10
        print(digito)
        temp //= 10