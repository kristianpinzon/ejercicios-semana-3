#16 Control de Inventario y Ventas
stock = 20

while stock > 0:
    print(f"Stock actual: {stock} unidades")
    cantidad = int(input("Ingrese la cantidad a ser vendida: "))
    
    if cantidad > stock:
        print("Error, La venta supera el stock disponible\n")
    elif cantidad <= 0:
        print("Error, Debe ingresar una cantidad mayor a 0\n")
    else:
        stock -= cantidad
        print(f"Venta realizada. Unidades restantes: {stock}\n")

print("El stock ha quedado en 0. Fin del programa.")