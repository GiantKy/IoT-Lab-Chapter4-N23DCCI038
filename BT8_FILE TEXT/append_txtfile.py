f = open('test.txt', 'a')  # Chế độ append
for i in range(6, 11):
    data = f'Added Line {i}!\n'
    f.write(data)
f.close()
print('Đã ghép thêm 5 dòng.')
