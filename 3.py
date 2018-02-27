# Largest prime factor

from utils import sieve
from math import sqrt

target = 600851475143
primes = sieve(int(sqrt(target)))

p_index = 0
target_factor = []

while True:
    p = primes[p_index]
    if target < p:
        break
    elif target % p == 0:
        target /= p
        target_factor.append(p)
    else:
        p_index += 1

print target_factor
