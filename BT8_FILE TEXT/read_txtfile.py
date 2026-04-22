# === readline() ===
print('--- readline() ---')
f = open('test.txt', 'r')
print(repr(f.readline()))  # Dòng 1
print(repr(f.readline()))  # Dòng 2
f.close()

# === readlines() ===
print('\n--- readlines() ---')
f = open('test.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line.strip())
f.close()

# === read() ===
print('\n--- read() ---')
f = open('test.txt', 'r')
data = f.read()
print(data)
f.close()
