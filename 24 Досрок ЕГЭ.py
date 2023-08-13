f = open("24.2.txt")
s = f.readline()
for uneven in "13579BDF":
    s = s.replace(uneven, "*")
a = s.split("*")
res = []
for i in a:
    if i.count("E") >= 5:
        res.append(i)
print(len(max(res)))
