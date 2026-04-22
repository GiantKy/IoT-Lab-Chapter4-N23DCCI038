import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data1 = {'x': list(range(1,10)), 'y': [i**2 for i in range(1,10)]}
data2 = {'x': list(range(1,10)), 'y': [i**1.5 for i in range(1,10)]}

# Đồ thị 1: đường đỏ (data1)
plt.plot(data1['x'], data1['y'], color='r', linewidth=2, label='Y = X²')

# Đồ thị 2: phân tán tam giác xanh (data2)
plt.scatter(data2['x'], data2['y'], marker='^', color='b', s=80, label='Y = X^1.5')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Kết hợp Line + Scatter')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('plt_3.png', dpi=150)
print('Saved: plt_3.png')
