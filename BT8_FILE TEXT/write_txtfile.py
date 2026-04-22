f = open('test.txt', 'w')
for i in range(1, 6):
    data = f'Line {i}\n'
    f.write(data)
f.close()
print('Đã ghi 5 dòng vào test.txt')
