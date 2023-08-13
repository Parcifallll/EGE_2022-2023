# определить максимальное расстояние между двумя одинаковыми буквами в строке
f = open("24.3.txt")
max_dist = []
for s in f:
    if s.count("p") < 20:
        for letter in set(s):
            max_dist.append(s.rfind(letter) - s.find(letter))
print(max(max_dist))
