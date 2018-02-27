from utils import sieve

limit = 2000000
primes = sieve(limit)
print sum(primes)
