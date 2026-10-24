#17 Totalizador de Carrito de Compras
total = 0

while True:
    precio = float(input("Ingrese el precio del producto (0 para terminar): $"))
    if precio == 0:
        break
    elif precio < 0:
        print("Error: El precio no puede ser negativo.")
    else:
        total += precio

print(f"\nTotal a pagar: ${total}")