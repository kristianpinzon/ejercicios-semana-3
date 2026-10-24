#28 Detector de Números Primos
numero = int(input("Ingrese un número entero positivo: "))

if numero <= 1:
    print(f"El número {numero} no es primo.")
else:
    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
            
    if divisores == 2:
        print(f"El número {numero} ES primo.")
    else:
        print(f"El número {numero} NO es primo (tiene {divisores} divisores).")