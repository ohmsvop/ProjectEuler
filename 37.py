# Truncatable primes
from utils import sieve

limit = 1000000
primes = sieve(limit)
primes_set = set(primes)

def check(p):
    p = str(p)
    n = len(p)
    if n == 1:
        return False
    for s in range(1,n):
        if int(p[s:]) not in primes_set:
            return False
        if int(p[:s]) not in primes_set:
            return False
    return True

candidate = [p for p in primes if check(p)]
print(sum(candidate))
