def R(N):
    n = bin(N)[2:]
    n = n + str(n.count("1") % 2)
    n = n + str(n.count("1") % 2)
    return int(n, 2)



for N in range(1, 1000):
    if R(N) > 720:
        print(R(N))
        break
