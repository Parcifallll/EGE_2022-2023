f = open("26_4_DyR5lZ6.txt")
cur_len = 0
time = []
max_len = 0
for s in f:
    a, b = map(int, s.split())
    time.append([a, b])
cnt = 0
cur_len = 0
for i in range(len(time) - 1):
    if cnt == 0:
        if time[i][1] >= time[i + 1][0]:
            cnt += 1
            early_time = time[i][1]
            max_len = max(max_len, cnt)
    else:
        if early_time >= time[i + 1][0]:
            cnt += 1
            max_len = max(max_len, cnt)
        else:
            cnt = 0
print(max_len)
