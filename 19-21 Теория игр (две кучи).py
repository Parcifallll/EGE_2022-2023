from functools import lru_cache


def moves(x, s):
    return (x + 2, s), (x, s + 2), (x * 2, s), (x, s * 2)


@lru_cache
def res(x, s):
    if any(sum(m) >= 73 for m in moves(x, s)): return "win1"
    # if any(res(*m) == "win1" for m in moves(x, s)): return "19task"
    # Если 19 задание - найти НЕУДАВШИЙСЯ ход Полины(1)
    if all(res(*m) == "win1" for m in moves(x, s)): return "loss1"
    if any(res(*m) == "loss1" for m in moves(x, s)): return "win2"
    if all(res(*m) == "win2" or res(*m) == "win1" for m in moves(x, s)): return "loss12"


s = 4
a = []
for x in range(1, 69):
    if res(x, s) == "loss12":
        a.append(x)
print(min(a), max(a))
