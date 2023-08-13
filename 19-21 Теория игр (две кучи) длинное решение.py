def win1(x, s):
    return (x + 2 + s) >= 81 or (x * 4 - 4 + s) >= 81 or (x + s * 4 - 4) >= 81


def loss1(x, s):
    return (not (win1(x, s)) and win1(x + 2, s) and win1(x, s + 2) and win1(x * 4 - 4, s) and win1(x, s * 4 - 4))


def win2(x, s):
    return loss1(x + 2, s) or loss1(x, s + 2) or loss1(x * 4 - 4, s) or loss1(x, s * 4 - 4)


def loss12(x, s):
    return ((win1(x + 2, s) or win2(x + 2, s)) and
            (win1(x, s + 2) or win2(x, s + 2)) and
            (win1(x * 4 - 4, s) or win2(x * 4 - 4, s)) and
            (win1(x, s * 4 - 4) or win2(x, s * 4 - 4)) and
            (win2(x + 2, s) or win2(x, s + 2) or
             win2(x * 4 - 4, s) or win2(x, s * 4 - 4)))


x = 7
for s in range(1, 74):
    if loss12(x, s):
        print(s)
