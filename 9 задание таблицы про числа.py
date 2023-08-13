f = open("9.txt")
cnt = 0
for p in f:
    s = list(map(int, p.split()))
    max_n = max(s)
    min_n = min(s)
    s.remove(max(s))
    s.remove(min(s))
    numbers = []
    for number in s:
        numbers.append(number ** 2)
    if (max_n + min_n) ** 2 > sum(numbers):
        cnt += 1
print(cnt)
