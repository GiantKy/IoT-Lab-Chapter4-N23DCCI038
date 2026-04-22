import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
from datetime import datetime

# === Mô phỏng DHT-11 (thay vì Adafruit_DHT) ===
class SimDHT11:
    def __init__(self, base_temp=25.0, base_hum=60.0):
        self.base_temp = base_temp
        self.base_hum = base_hum
    def read(self):
        t = round(random.gauss(self.base_temp, 1.5), 1)
        h = round(random.gauss(self.base_hum, 3.0), 1)
        return h, t

sensor = SimDHT11(base_temp=28.0, base_hum=65.0)
max_points = 50

# Thu thập dữ liệu
temps, hums, timestamps = [], [], []
for i in range(max_points):
    h, t = sensor.read()
    temps.append(t)
    hums.append(h)
    timestamps.append(i)
    print(f'  Mẫu {i+1}/{max_points}: Temp={t}°C, Hum={h}%')

# Vẽ đồ thị 2 subplot (theo Slide Bài 3.2)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

ax1.plot(timestamps, temps, 'r-', linewidth=1.5, label='Nhiệt độ (°C)')
ax1.axhline(y=30, color='orange', linestyle='--', label='Ngưỡng 30°C')
ax1.fill_between(timestamps, 30, [max(t, 30) for t in temps],
                  alpha=0.3, color='red', label='Vùng quá nhiệt')
ax1.set_ylabel('Nhiệt độ (°C)')
ax1.set_title('Mô phỏng DHT-11 — Trực quan hóa dữ liệu (Slide Bài 3.2)')
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)

ax2.plot(timestamps, hums, 'b-', linewidth=1.5, label='Độ ẩm (%)')
ax2.axhline(y=70, color='orange', linestyle='--', label='Ngưỡng 70%')
ax2.set_ylabel('Độ ẩm (%)')
ax2.set_xlabel('Sample')
ax2.legend(loc='upper right')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('temp_visualization.png', dpi=150)
print(f'Saved: temp_visualization.png ({max_points} mẫu)')
