from gpiozero import LED

led = LED(20)  # GPIO 20

while True:
    led.on()
