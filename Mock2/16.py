from functools import lru_cache


@lru_cache
def f(n):
    if n >= 2023:
        return n
    else:
        return n // 3 + f(n + 2)
print(f(2015) - f(2018))
