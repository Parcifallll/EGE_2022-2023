def Del(n, m):
    return n % m == 0


max_A = 0

for A in range(1, 100):
    # flag = True
    for x in range(1, 100):
        if (Del(x, 15) <= ((not (Del(x, A))) <= (not (Del(x, 3))))) == 0:
            # flag = False
            break
    else:
        max_A = A
    # if flag:
    #     max_A = A
print(max_A)
# Изначально функция истинна при всех значениях, значит сохраняем где при всех х А будет верно
# либо (2 способ) через flag