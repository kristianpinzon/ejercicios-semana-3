#30 Máximo Común Divisor (MCD) por Algoritmo de Euclides
numa = int(input("Ingrese el primer número entero positivo: "))
numb = int(input("Ingrese el segundo número entero positivo: "))

num1, num2 = numa, numb

while numb != 0:
    residuo = numa % numb
    numa = numb
    numb = residuo

print(f"El Máximo Común Divisor de {num1} y {num2} es: {numa}")