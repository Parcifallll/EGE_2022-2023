f = open("24.1.txt")
s = f.readline()
for i in "ABC":
    s = s.replace(i, "*")
s = s.replace("**", "* *").split()
print(len(max(s, key=len)))
# заменяем на звездочку именно через ПРОБЕЛ потому что у нас в концах строки еще +1 и + 1 символ