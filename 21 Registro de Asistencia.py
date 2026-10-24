#21 Registro de Asistencia
presentes = 0
ausentes = 0

while True:
    estado = input("Ingrese asistencia ('P': Presente, 'A': Ausente, 'F': Fin): ").strip().upper()
    
    if estado == 'F':
        break
    elif estado == 'P':
        presentes += 1
    elif estado == 'A':
        ausentes += 1
    else:
        print("Opción no válida. Ingrese P, A o F.")

print("\nRESUMEN DE ASISTENCIA")
print(f"Aprendices presentes: {presentes}")
print(f"Aprendices ausentes: {ausentes}")