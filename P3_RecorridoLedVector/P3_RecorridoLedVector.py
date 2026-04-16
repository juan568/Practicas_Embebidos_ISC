import RPi.GPIO as GPIO
import time

# Configuración de pines y tiempos
pines = [17, 27, 22, 10, 9]
retardo = 0.2

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # Configuramos todos los pines del vector en un solo ciclo
    for pin in pines:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    print("Sistema listo. Iniciando recorrido...")

def recorrido():
    while True:
        # IDA: Recorre el vector de izquierda a derecha
        print("Ida...")
        for pin in pines:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(retardo)
            GPIO.output(pin, GPIO.LOW)

        # VUELTA: Recorre el vector de derecha a izquierda
        print("Vuelta...")
        for pin in reversed(pines):
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(retardo)
            GPIO.output(pin, GPIO.LOW)

if __name__ == "__main__":
    setup()
    try:
        recorrido()
    except KeyboardInterrupt:
        print("\nDetenido por el usuario")
    finally:
        GPIO.cleanup()
        print("Pines liberados correctamente.")
