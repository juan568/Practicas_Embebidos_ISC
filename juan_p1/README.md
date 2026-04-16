# Repositorio de Prácticas - Embebidos ISC (Grupo 8S21)

### Integrantes del equipo
* **Arath Hernandez Camacho** - Matrícula: 226020019
* **Gustavo Efren Jimenez Valencia** - Matrícula: 226020090
* **Pamela Jhatdzarhy Perez Gomez** - Matrícula: 226020038
* **Juan Manuel Perez Medina** - Matrícula: 226020139 

---

## Práctica 1: Parpadeo del LED
### Descripción
Control de un LED físico mediante los pines GPIO de la Raspberry Pi 4B utilizando Python. En esta práctica se configuró un circuito básico para realizar un parpadeo intermitente.

### Configuración de Hardware
* **Pin de señal:** Pin físico 12 (GPIO 18 en modo BCM).
* **Resistencia:** 220Ω conectada a GND.
* **LED:** Rojo

### Instrucciones de ejecución
1. `cd ~/practicas_embebidos/P1_LedBlink`
2. `source env_blink/bin/activate`
3. `python P1_LedBlink.py`

---

## Práctica 2: Semáforo de Leds

### Descripción
Simulación de un semáforo de tránsito utilizando tres LEDs (Verde, Amarillo y Rojo). El programa implementa una secuencia de 10 segundos para Rojo/Verde y parpadeo para el Amarillo.

### Configuración de Hardware
* **LED Verde:** GPIO 17 | **Amarillo:** GPIO 27 | **Rojo:** GPIO 22
* **Resistencias:** 220Ω conectada a GND.

### Instrucciones de ejecución
1. `cd ~/practicas_embebidos/P2_SemaforoLeds`
2. `source ../P1_LedBlink/env_blink/bin/activate`
3. `python P2_Semaforo.py`
