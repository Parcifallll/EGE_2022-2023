f = open("22.txt")
a = [0] * 81
for s in f:
    s2 = s.replace(";", " ").split()
    a[int(s2[0])] = int(s2[1]) + max(a[int(x)] for x in s2[2:])
print(max(a))
# На ЕГЭ 99% не попадется
