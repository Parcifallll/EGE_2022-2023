num = "0123456789ABCDEFG"
for x in num:
    s = (int(f"18{x}AE", 17) + int(f"733{x}C", 17))
    if s % 13 == 0:
        print(s / 13)
        break
