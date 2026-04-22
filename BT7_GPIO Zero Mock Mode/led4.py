from gpiozero import LED
from time import sleep

# Dictionary quản lý 3 LED (theo Slide Bài 1.1)
leds = {
    "red": LED(5),
    "yellow": LED(6),
    "green": LED(13),
}

# Nháy tuần tự từng LED
for name, led in leds.items():
    print(f'Nháy LED {name}...')
    led.blink(on_time=1, off_time=1)
    sleep(2)
    led.off()

print('Hoàn thành nháy 3 LED.')

