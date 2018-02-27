# 10001st prime

# pn ~ n/log(n)
# 200000./log(200000) = 16385

from utils import sieve
from math import log
n = 200000
primes = sieve(n)
print len(primes)
print primes[10000]
