from itertools import product

for n in range(5, 7):
    for x in product("0123456789ABCDEF", repeat=n):
        x1 = "".join(x)
        if x1[:3] == "A15" and x1[-1] == "F" and int(x1, 16) % 149 == 0:
            print(x1, int(x1, 16) // 149)

# for i in range(149, int("ffffff", 16) + 1, 149):
#     num16 = hex(i)[2:]
#     if len(num16) >= 5 and num16[:3] == "a15" and num16[-1] == "f":
#         print(num16.upper(), i // 149)
#А15Ш*F дел на 149 среди шестнадц. чисел
#Задача с рулетки(на ЕГЭ никогда не бывает)