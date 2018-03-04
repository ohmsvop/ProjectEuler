# Champernowne's constant
from numpy import product

n = 0
i_list = [10**i for i in range(7)]
d = {}

for i in range(1, 1000000):
     s = str(i)
     l = len(s)
     for di in i_list:
         if n < di and di <= n+l:
            d[di] = int(s[di-n-1])
     n += l
     if n > 1000000:
         break
print d
print product(d.values())
