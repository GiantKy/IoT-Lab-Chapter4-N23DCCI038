import matplotlib
matplotlib.use('Agg')  # Backend headless cho QEMU
import matplotlib.pyplot as plt

# Dữ liệu x, y
data = {
    "x": list(range(1, 10)),
    "y": [i**2 for i in range(1, 10)]
}

# Vẽ biểu đồ đường
plt.plot(data['x'], data['y'], color='blue', linewidth=2)
plt.xlabel('X')
plt.ylabel('Y = X²')
plt.title('Biểu đồ đường — Y = X²')
plt.grid(True, alpha=0.3)
plt.savefig('plt_1.png', dpi=150)
print('Saved: plt_1.png')

