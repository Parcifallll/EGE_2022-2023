from functools import lru_cache


def moves(x):
    return (x + 1), ((x * 2) - 1)


@lru_cache
def res(x):
    if any(m >= 55 for m in moves(x)): return "win1"
    # if any(res(m) == "win1" for m in moves(x)): return "19"
    if all(res(m) == "win1" for m in moves(x)): return "loss1"
    if any(res(m) == "loss1" for m in moves(x)): return "win2"
    if all(res(m) == "win1" or res(m) == "win2" for m in moves(x)): return "loss12"
    if any(res(m) == "loss12" for m in moves(x)):return "win12"


for x in range(2, 55):
    if res(x) == "win12":
        print(x)

