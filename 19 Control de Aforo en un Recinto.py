# 19 Control de Aforo en un Recinto
capacidad_maxima = 5
personas_adentro = 0

while personas_adentro < capacidad_maxima:
    input("Presione ENTER para registrar el ingreso de una persona ")
    personas_adentro += 1
    print(f"Ingresó 1 persona. Personas en el recinto: {personas_adentro}/{capacidad_maxima}\n")

print("Aforo completo")