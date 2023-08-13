f=open("27_2_A_dz_lldjKZy.txt")
n=int(f.readline())
a=[]
for s in f:
    a.append(int(s))
summ_51=[]
for i in range(len(a)):
    for j in range(i+1,n):
        if sum(a[i:j+1]) % 51 ==0:
            summ_51.append(sum(a[i:j+1]))
print(max(summ_51))

