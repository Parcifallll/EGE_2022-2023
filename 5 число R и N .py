def r(n):
    n2 = bin(n)[2:]
    n2 += n2[-1]
    n2 += str(bin(n)[2:].count("1") % 2)  # дописываем 0, если чет 1, 0 если нечет
    n2 + str(n2.count("1") % 2)  # остаток от дел суммы всех чисел(единиц) на два
    return int(n2, 2)


for x in range(1, 1000):
    if r(x) > 153:
        print(x)
        break
