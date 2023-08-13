f = open("17.4 (1).txt")
elements = [int(x) for x in f]
min_el = min([i for i in elements if str(i)[-1] == "7"])
sum_pairs = []

for i in range(len(elements) - 1):
    cnt = 0
    if str(elements[i])[-1] == str(elements[i + 1])[-1]:
        if elements[i] % 7 == 0:
            cnt += 1
        if elements[i + 1] % 7 == 0:
            cnt += 1
        if cnt == 1 and ((elements[i] ** 2 + elements[i + 1] ** 2) <= min_el ** 2):
            sum_pairs.append(elements[i] ** 2 + elements[i + 1] ** 2)
print(len(sum_pairs), max(sum_pairs))
# найти кол-во пар где оба числа оканчиваются на одну цифру(когда отриц числа - берем МОДУЛЬ % 10 == 7, либо str()[-1]
