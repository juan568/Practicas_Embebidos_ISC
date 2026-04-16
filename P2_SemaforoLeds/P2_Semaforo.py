import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_VERDE = 17
LED_AMARILLO = 27
LED_ROJO = 22

GPIO.setup(LED_VERDE, GPIO.OUT)
GPIO.setup(LED_AMARILLO, GPIO.OUT)
GPIO.setup(LED_ROJO, GPIO.OUT)

try:
    while True:
        # Verde
        print("Encendido: VERDE")
        GPIO.output(LED_ROJO, GPIO.LOW) # Asegura apagar el rojo al reiniciar
        GPIO.output(LED_VERDE, GPIO.HIGH)
        GPIO.output(LED_AMARILLO, GPIO.LOW)
        time.sleep(10)
        GPIO.output(LED_VERDE, GPIO.LOW)

        # Amarillo parpadeando
        print("Encendido: AMARILLO (Parpadeo)")
        for i in range(5):
            GPIO.output(LED_AMARILLO, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_AMARILLO, GPIO.LOW)
            time.sleep(1)

        # Rojo
        print("Encendido: ROJO")
        GPIO.output(LED_ROJO, GPIO.HIGH)
        time.sleep(10)

except KeyboardInterrupt:
    print("\nPrograma detenido")

finally:
    GPIO.cleanup()
