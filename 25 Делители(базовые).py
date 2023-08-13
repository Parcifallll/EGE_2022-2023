def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for i in range(904528, 912345):
    if i % 11 != 0 or i % 7 == 0:
        continue
    dividers = []
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if isPrime(j):
                dividers.append(j)
            #     добавляем первые делители т.к. идем до корня из числа
            if isPrime(i // j):
                dividers.append(i // j)
    #             Добавляем второй делитель
    if len(set(dividers)) > 5:
        # Проверяем уникальность каждого делителя
        print(i, sum(dividers))
# Если корень извлекается - НЕЧЕТНОЕ количество делителей, иначе ЧЕТНОЕ.
#НА ЕГЭ ДЕЛИТЕЛИ ВСЕГДА ПРОСТЫЕ, НО 90% ДАДУТ МАСКИ ЧИСЛА