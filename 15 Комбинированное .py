def Del(n, m):
    return n % m == 0


D = list(range(30, 46))
for A in range(1, 1000):
    for x in range(1, 1000):
        if (((not (Del(x, 7))) and x not in [52, 60, 68]) <= ((abs(x - 25) <= 10) <= (x in D)) or (x & A != 0)) == 0:
            break
    else:
        print(A)
        break

# Егэ- 2022(гораздо сложнее)
# Просят ЧИСЛО А(не длину - иначе А это список)