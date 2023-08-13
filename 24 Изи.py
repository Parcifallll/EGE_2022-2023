f = open("24.3.txt")
cnt = 0
for s in f:
    for vowel in "EYUIOA":
        s = s.replace(vowel, "*")
    for even_n in "02468":
        s = s.replace(even_n, "+")
    if len(s) <= 30 and s.count("*") == 10 and "+" not in s:
        cnt += 1
print(cnt)
