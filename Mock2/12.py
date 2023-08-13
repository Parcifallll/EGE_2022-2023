for n in range(1, 10000):
    s = ">" +  33 * "8" + 54 * "4" + n * "2"
    while ">2" in s or ">4" in s or ">8" in s:
        if ">2" in s:
            s = s.replace(">2", "28>", 1)
        if ">4" in s:
            s = s.replace(">4", "22>8", 1)
        if ">8" in s:
            s = s.replace(">8", "244>", 1)
    if len(str(sum([int(i) for i in s if i != ">"]))) == 5:
        print(n)
        break
