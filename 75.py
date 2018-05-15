# Singular integer right triangles
from utils import gcd

# (a, b, c) = (m**2 - n**2, 2*m*n, m**2 + n**2), m > n > 0
# L = 2*m**2+2*m*n

L_max = 1500000
L = [0]*(L_max+1)

for m in range(2, 1000):
    for n in range(1, m):
        if gcd(m,n) == 1 and (m+n) % 2 == 1:
            p = 2*m**2+2*m*n
            pm = p
            while pm <= L_max:
                L[pm] += 1
                pm += p

print L.count(1)

