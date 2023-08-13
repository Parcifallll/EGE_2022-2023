for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((x >= 17) or (3 * x < y)) or (y * x < A)) == 0:
                flag = False
                break
        if flag == False:
            break
    if flag:
        print(A)
        break
# Требуются только положительные - если функция ложна
# Т.е. flag =0 причем в обоих циклах(иначе будет работать медленнее)
# Обращаем внимание на условие - могут попросить НЕОТРИЦАТЕЛЬНЫЕ значения