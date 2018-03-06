# Goldbach's other conjecture

from utils import sieve

limit = 10000
primes = sieve(limit)
primes_set = set(primes)

limit_s = int((limit/2)**0.5)
squares = [2*i**2 for i in range(limit_s)]

sum_ps = set()
for s in squares:
    for p in primes_set:
        sum_ps.add(p+s)

candidate = []
for i in range(3, limit, 2):
    if i not in primes_set and i not in sum_ps:
        candidate.append(i)

print candidate

