f = open("27_1_a.txt")

n = int(f.readline())
max_sum = 0
razn = []
for s in f:
    a, b = map(int, s.split())
    max_sum += max(a, b)
    if abs(a - b) != 0:
        razn.append(abs(a - b))
razn.sort()
for i in razn:
    if (max_sum - i) % 5 == 0 and (max_sum - i) % 11 == 0:
        break
    elif (max_sum - i) % 5 == 0 or (max_sum - i) % 11 == 0:
        max_sum -= i
        print(max_sum)
        break
