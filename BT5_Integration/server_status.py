from sense_emu import SenseHat
import time

sense = SenseHat()
sense.clear()

# ===== MAP VALUE =====
def map_value(val, in_min, in_max):
    val = (val - in_min) / (in_max - in_min) * 8
    return max(0, min(8, int(val)))

# ===== DRAW BAR =====
def draw_bar(y_start, y_end, cols, color):
    for y in range(y_start, y_end + 1):
        for x in range(8):
            if x < cols:
                sense.set_pixel(x, y, color)
            else:
                sense.set_pixel(x, y, (0, 0, 0))

# ===== LOOP =====
while True:
    temp = sense.get_temperature()
    hum = sense.get_humidity()

    # ===== BAR TEMP (hàng 0-2) =====
    temp_cols = map_value(temp, 15, 40)
    draw_bar(0, 2, temp_cols, (255, 0, 0))

    # ===== BAR HUM (hàng 3-5) =====
    hum_cols = map_value(hum, 20, 90)
    draw_bar(3, 5, hum_cols, (0, 0, 255))

    # ===== STATUS (hàng 6-7) =====
    if temp > 35 and hum > 80:
        status = (255, 0, 0)
        msg = "DANGER!"
    elif temp > 30 or hum > 80:
        status = (255, 255, 0)
        msg = "WARNING"
    else:
        status = (0, 255, 0)
        msg = "OK"

    draw_bar(6, 7, 8, status)

    # ===== HOT MESSAGE =====
    if temp > 30:
        sense.show_message("HOT!", text_colour=(255, 0, 0))

    print(f"Temp: {temp:.1f} | Hum: {hum:.1f} | Status: {msg}")

    time.sleep(1)