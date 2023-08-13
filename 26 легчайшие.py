f = open("26.1.txt")
n, k = map(int, f.readline().split())
n = 10000
new_list = [int(f.readline()) for i in range(n)]

new_list.sort()
new_list = new_list[k:]
new_list.sort(reverse=True)
new_list = new_list[k:]
print(new_list[-1], sum(new_list) // len(new_list))
# убираем наименьшие и наибольшие 1235 символов
