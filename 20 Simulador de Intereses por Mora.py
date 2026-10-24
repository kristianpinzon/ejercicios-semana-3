#20 Simulador de Intereses por Mora
deuda = float(input("Ingrese el valor inicial de la deuda: $"))
meses = int(input("Ingrese el número de meses en mora: "))

TASA_INTERES = 0.05

for mes in range(1, meses + 1):
    deuda += deuda * TASA_INTERES
    print(f"Mes {mes}: Deuda acumulada = ${deuda}")

print(f"\nSaldo final adeudado: ${deuda}")