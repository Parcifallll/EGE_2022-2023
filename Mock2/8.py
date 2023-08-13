from itertools import *
cnt = 0
for x in product("АВСЕН", repeat=4):
   cnt += 1
   if "".join(x) == "СЕВА":
       print(cnt)
       break