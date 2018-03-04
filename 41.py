# Pandigital prime

# n != 8, 9

from utils import sieve

primes = sieve(8000000)

def check(n):
    n = str(n)
    l = len(n)
    if "0" in n:
        return False
    for i in range(1, l+1):
        if str(i) not in n:
            return False
    return True

candidate = [p for p in primes if check(p)]
print candidate[-1]
