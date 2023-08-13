f = open("24.3.txt")
s = f.readline()
a = s.split("O")
max_len = 0
for i in range(len(a) - 1):
    max_len = max(max_len, len(a[i] + "O" + a[i + 1]))
print(max_len)
# Сплитаем по О затем рассматриваем a[i] и  a[i+1] строчки
# добавляем длину общей строки (a[i] + "O" + a[i + 1])
