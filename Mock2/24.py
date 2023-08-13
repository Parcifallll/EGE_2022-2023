f = open("24.txt")
s = f.readline()
for i in "UMS":
    s = s.replace(i, "*")
s = s.split("**")
max_len = []
for i in s:
    max_len.append(len(i))
    if len(i) == 98:
        print(i)
print(max(max_len))
