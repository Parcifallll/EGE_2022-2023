print("a b c d")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if (not (c <= b) and (d <= a) != (b and c and d and not (a))):
                    print(a, b, c, d)
