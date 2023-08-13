f = open("9.txt")
cnt = 0
for s in f:
    num = list(map(int, s.split()))
    if len(num) == len(set(num)):
        max_num = max(num)
        min_num = min(num)
        num.remove(max_num)
        num.remove(min_num)
        if ((max_num + min_num) * 3) >= (sum(num) * 2):
            cnt += 1
print(cnt)