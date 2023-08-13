# 143*9*
cnt = 0
for x in range(1456, 1000001, 56):
    if x % 56 == 0:
        if str(x)[:3] == "143" and "9" in str(x):
            print(x, x // 42)
