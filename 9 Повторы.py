f = open("9.txt")
cnt = 0
for s in f:
     a = list(map(int,s.split()))
     if len(set(a)) == 4:
         repeat = []
         unrepeat = []
         for x in a:
             if a.count(x) ==1:
                 unrepeat.append(x)
             else:
                 repeat.append(x)
         if sum(repeat) < sum(unrepeat):
             cnt += 1
print(cnt)
# В каждой строке 6 чисел, найти кол-во строк в которых 4  различных числа и сумма повторов меньше суммы неповторов