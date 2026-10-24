#22 Temporizador de Timeout de Servidor
import time

print("Conectando al servidor...")
for segundo in range(1, 6):
    print(f"Esperando respuesta... {segundo}s")
    time.sleep(1)

print("Tiempo de espera agotado (Timeout)")