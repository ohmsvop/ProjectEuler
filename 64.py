# Odd period square roots
from utils import is_square

def continued_fraction(n):
    m = 0
    d = 1
    a = a0 = int(n**0.5)
    expansion = [a0]
    while a != 2*a0:
        m = d * a - m
        d = (n-m**2)/d
        a = (a0+m)/d
        expansion.append(a)
    return expansion
    
max_N = 10000
n = 0
for i in range(max_N+1):
    if is_square(i):
        continue
    e = continued_fraction(i)
    if len(e) % 2 ==0:
        n += 1
print n
