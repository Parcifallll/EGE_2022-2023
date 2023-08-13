def isSquare(x):
    return x ** 0.5 % 1 == 0


def isFib(x):
    return bool(isSquare(5 * x ** 2 + 4) + isSquare(5 * x ** 2 - 4))


cnt = 0
for x in range(56789, 67891):
    flag = False
    dividers = [i for i in range(2, x) if x % i == 0]
    for s in range(len(dividers) - 2):
        if isFib(dividers[s]) and isFib(dividers[s + 1]) and isFib(dividers[s + 2]):
            print(x)
            cnt += 1
            break
    if cnt == 4:
        break

# Требуется найти 4 наим числа, делители которых представляют ряд >= 3 чисел Фибоначчи подряд