from fnmatch import fnmatch
# Маска 154*8* и число делится на 99 и не превышает 1000000(миллион)
for x in range(99, 10 ** 6 + 1, 99):
    if fnmatch(str(x), "154*8*"):
        print(x, x // 99)
