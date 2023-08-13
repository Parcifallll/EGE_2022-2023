# сначала чертим в кумире, потом находим уравнения прямых тут и находим кол-во точек
from math import *
cnt=0
for x in range(0,200):
    for y in range(0,200):
        if x > 0 and y> tan(radians(30))*x and y < tan(radians(150))*x + 123:
            cnt+=1
print(cnt)