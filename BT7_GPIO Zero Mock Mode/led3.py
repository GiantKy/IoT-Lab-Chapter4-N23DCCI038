from gpiozero import LED

led = LED(20)

while True:
    cmd = input('Nhập lệnh (on/off/exit): ').strip().lower()
    if cmd == 'on':
        led.on()
        print('LED đã BẬT')
    elif cmd == 'off':
        led.off()
        print('LED đã TẮT')
    elif cmd == 'exit':
        led.off()
        print('Thoát chương trình.')
        break
    else:
        print(f'Lệnh không hợp lệ: {cmd}')
