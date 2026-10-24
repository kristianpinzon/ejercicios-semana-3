#26 Buscador de Valor Máximo
maximo = None

print("Ingrese números enteros (ingrese 0 para terminar):")
while True:
    numero = int(input("Número: "))
    
    if numero == 0:
        break
        
    if maximo is None or numero > maximo:
        maximo = numero

if maximo is not None:
    print(f"\nEl número más alto ingresado fue: {maximo}")
else:
    print("\nNo se ingresaron números válidos antes del 0.")