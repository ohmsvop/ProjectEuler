# Smallest multiple

from utils import lcm

limit = 20
l = 1
for i in range(1,limit+1):
    l = lcm(l, i)
print l
