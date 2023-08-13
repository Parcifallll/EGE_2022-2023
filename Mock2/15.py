def func(x, y, A):
    return (x > 42) or (y < x) or (3 * x < A)

for A in range(1, 10000):
    if all(func(x, y, A) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break

