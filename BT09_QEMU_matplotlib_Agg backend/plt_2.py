import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = {
    "x": list(range(1, 10)),
    "y": [i**2 for i in range(1, 10)]
}

# Biểu đồ phân tán với marker hình tròn
plt.scatter(data['x'], data['y'], marker='o', color='red', s=80)
plt.xlabel('X')
plt.ylabel('Y = X²')
plt.title('Biểu đồ phân tán — Y = X²')
plt.grid(True, alpha=0.3)
plt.savefig('plt_2.png', dpi=150)
print('Saved: plt_2.png')
