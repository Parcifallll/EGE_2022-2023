f = open("24.4.txt")
s = f.readline()
for i in "TR":
    s = s.replace(i, "S")
s = s.replace("U", "A")
cnt = 0
for x in range(1, 100):
    if "AS" * x in s:
        cnt += 1
print(cnt)
# в файле только буквы STARU, найти кол-во сочетаний ГС(глас-соглас), причем СГ не в счет