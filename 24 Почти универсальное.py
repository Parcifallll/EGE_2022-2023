f = open("24.2.txt")
s = f.readline()
curr_len, max_len, cnt_E = 0, 0, 0
for i in range(len(s)):
    if s[i] in "02468ACE":
        curr_len += 1
        if s[i] == "E":
            cnt_E += 1
        if cnt_E >= 5:
            max_len = max(curr_len, max_len)
    else:
        curr_len = 0
        cnt_E = 0
print(max_len)