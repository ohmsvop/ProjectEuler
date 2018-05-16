# Prime summations
# same as problem 31 & 76

from utils import sieve

primes = sieve(100)

target = 71
method = [0]*(target+1)
method[0] = 1

for p in primes:
    for i in range(p, target+1):
        method[i] += method[i - p]

print method[target]
