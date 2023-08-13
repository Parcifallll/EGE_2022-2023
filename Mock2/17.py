f = open("17.txt")
a = [int(i) for i in f]
min_n = 10000
for s in a:
    if len(str(s)) == 2 and s < min_n:
        min_n = s
sum_p = []
for i in range(len(a) - 1):
    if ((len(str(a[i])) == 2) + (len(str(a[i + 1])) == 2)) == 1:
        if (a[i] + a[i+1]) % min_n == 0:
            sum_p.append(a[i] + a[i + 1])
print(len(sum_p), max(sum_p))
