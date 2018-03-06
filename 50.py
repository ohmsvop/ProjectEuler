# Consecutive prime sum

from utils import sieve

limit = 1000000
primes = sieve(limit)
primes_set = set(primes)
n = 100
while n < 1000:
    for i in range(len(primes)-n):
        sum_p = sum(primes[i:i+n])
        if sum_p in primes_set:
            print primes[i], sum_p, n
            n += 1
        if sum_p > limit:
            n += 1
            break
