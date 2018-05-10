# Ordered fractions
from __future__ import division
from utils import gcd

max_d = 8
frac = 3/7
best_n, best_d = 0, 1

for d in range(10, 1000000):
    n = int(frac*d)
    if gcd(n,d) != 1:
        continue
    if n/d > best_n/best_d:
        best_n = n
        best_d = d

print best_n, best_d
