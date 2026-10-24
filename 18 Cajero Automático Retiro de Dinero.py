#18 Cajero Automático - Retiro de Dinero
saldo = 500000

while saldo > 0:
    print(f"Saldo disponible: ${saldo}")
    retiro = float(input("Ingrese el monto a retirar (0 para salir): $"))
    
    if retiro == 0:
        print("Transacción finalizada por el usuario.")
        break
    elif retiro < 0:
        print("Error: El monto no puede ser negativo.\n")
    elif retiro > saldo:
        print("Error: Fondos insuficientes.\n")
    else:
        saldo -= retiro
        print(f"Retiro exitoso. Retirado: ${retiro}\n")

print(f"Transacción finalizada. Saldo restante: ${saldo}")