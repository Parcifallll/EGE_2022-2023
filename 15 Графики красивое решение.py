def func(x, y, A):
    return (2 * x - y < A) or ((x > 55) or (y > 32))


for A in range(1, 1000):
    if all(func(x, y, A) for x in range(1, 100) for y in range(1, 1000)):
        print(A)
        break
# создаем через генератор пары ХУ и проверяем, чтобы все значения выражения в этих парах истинны
