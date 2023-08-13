import string
f = open("24.2.txt")
s = f.readline()
length = 1
lenghts = []
for i in range(len(s) - 1):
    if s[i] in "02468" and s[i + 1] in "02468":
        length += 1
    elif s[i] in "02468" and s[i + 1] == "7":
        length += 1
        lenghts.append(length)
        length = 1
    else:
        length = 1
print(max(lenghts))
# Найти мах строку из четных цифр и оканчивающихся на 7, в файле даны все буквы и все цифры
# Изначально подсчет идет с ЕДИНИЦЫ, тк его мы не прибавляем в процессе
# *сложнее ЕГЭ

# Хитрое решение(именно ДЛЯ этого номера)
f = open("24.2.txt")
s = f.readline()
for i in "1359" + string.ascii_letters:
    s = s.replace(i, " ")
s = s.replace("7", "* ")
s = s.split()
max_len = 1
for i in s:
    if i[-1] == "*":
        max_len = max(max_len, len(i))
print(max_len)
