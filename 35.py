# Circular primes

from utils import sieve

primes = sieve(1000000)
primes_set = set(primes)

def check(n):
    if set(str(n)).intersection(["0", "4", "6,", "8"]):
        return False
    l = len(str(n))
    for i in range(l-1):
        sn = str(n)
        sn = sn[1:] + sn[0]
        n = int(sn)
        if n not in primes_set:
            return False
    return True

candidate = []
for p in primes:
    if check(p):
        candidate.append(p)

print len(candidate)
