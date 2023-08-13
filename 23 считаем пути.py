def programs(start, end):
    if start > end or start == 23:
        return 0
    if start == end:
        return 1
    return programs(start + 1, end) + programs(start * 2, end)


# проверяем, не равен ли старт 23
# путь должен содержать число 66
#  если команда -1, то первым условием возвращаем сумму

print(programs(4, 66) * programs(66, 93))
