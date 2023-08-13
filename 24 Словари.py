f = open()
s = f.readline()
letters = {}
for i in range(len(s) - 1):
    if s[i + 1] == "M":
        if s[i] not in letters:
            letters[s[i]] = 1
        letters[s[i]] += 1
print(letters)
print(max(letters, key=letters.get))
# После вывода макс элемента проверяем нет ли такого же по частоте элемента среди letters
