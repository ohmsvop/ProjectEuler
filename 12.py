# Highly divisible triangular number

from utils import prime_factorization
from collections import Counter

max_divisor = 0
for i in range(2, 15000):
    p1 = prime_factorization(i)
    p2 = prime_factorization(i+1)
    p1.extend(p2)
    p1.remove(2)
    c = Counter(p1)
    divisor = 1
    for count in c.values():
        divisor *= (count+1)
    if divisor > max_divisor:
        max_divisor = divisor
        print max_divisor
    if divisor > 500:
        print i, i*(i+1)/2, c
        break
