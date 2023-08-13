f = open("12.txt")
s = f.readline()
a = s.split("7")
a = a[1:]
cnt = 0
vowel = "aeyuiojAEYUIOJ"
for i in a:
    if "0" in i:
        id = "7" + i[:i.index("0") + 1]
        if len(set(id)) == len(id) and 8 <= len(id) <= 11:
            flag = False
            for j in range(len(id) - 2):
                if id in vowel and id[j + 1] in vowel and id[j + 2] in vowel:
                    flag = True
                    break
            if flag:
                cnt += 1
print(cnt)


