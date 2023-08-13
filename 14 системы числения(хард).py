a = list(range(10))
a += [num for num in "abcdefghij"]
for x in a:
    s = int(f"13{x}CF", 20) + int(f"47GH{x}", 20)
    if s % 19 == 0:
        print(s // 19)
        break
