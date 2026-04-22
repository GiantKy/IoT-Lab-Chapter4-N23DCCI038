from gpiozero import LED
from signal import pause

led = LED(20)

led.blink(on_time=1, off_time=1)
pause()  # Chờ tín hiệu — không cần vòng lặp while
