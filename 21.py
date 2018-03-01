# Amicable numbers

from utils import prime_factorization

def sum_proper_divisor(n):
    pf = prime_factorization(n)
    sum_d = 1
    for p in pf:
        d = 0
        for i in range(pf[p]+1):
            d += p**i
        sum_d *= d
    sum_d -= n
    return sum_d

amicable = []
limit = 10000
for i in range(2, limit+1):
    j = sum_proper_divisor(i)
    if i != j:
        k = sum_proper_divisor(j)
        if i == k:
            amicable.append(i)

print sum(amicable)
