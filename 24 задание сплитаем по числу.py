from string import ascii_letters

# найти номера телефонов
f = open("24.1 (1).txt")
s = f.readline()
for i in ascii_letters:
    s = s.replace(i, " ")
a = s.split()
cnt = 0
for phone_number in a:
    if phone_number[0] == "8" and len(phone_number) == 11 and (int(phone_number[-1]) + int(phone_number[-2])) % 2 == 0:
        cnt += 1
print(cnt)
