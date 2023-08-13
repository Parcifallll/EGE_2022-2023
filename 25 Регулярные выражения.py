from re import *

# \d любой символ один раз, \d* любой символ любое кол-во раз
# 64*32?2
for x in range(102, 10 ** 6, 102):
    if fullmatch(r"64\d*32\d2", str(x)):
        print(x, x // 102)
