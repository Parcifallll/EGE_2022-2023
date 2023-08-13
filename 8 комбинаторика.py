from itertools import *

# берем set, потому что есть две одинаковые буквы
# склеиваем строки через join, потому что ищем два символа в списке из одних букв
cnt = 0
for i in set(permutations("карета", r=4)):
    if "аа" not in "".join(i):
        cnt += 1
print(cnt)
