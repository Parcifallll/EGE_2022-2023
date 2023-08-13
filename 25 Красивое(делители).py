max_del = [0, 0]
for i in range(84052, 84130 + 1):
    dividers = []
    for j in range(2, int(i ** 0.5) + 1):
        if j * j == i:
            dividers.append(j)
        elif i % j == 0:
            dividers.append(j)
            dividers.append(i // j)
    if max_del[0] < len(dividers):
        max_del[0] = len(dividers)
        max_del[1] = i
print(*max_del)
