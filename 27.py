# Quadratic primes
# n2 + an + b
# b is prime

from utils import sieve

primes = sieve(3000000)
primes_set = set(primes)

def check_prime_chain(a,b):
    n = 0 
    while True:
        k = n**2 + a*n + b
        if k in primes_set:
            n += 1
        else:
            break
    return n

max_a, max_b = 0,0
max_chain = 0
# b = primes < 1000
possible_b = primes[:168] + [ -i for i in primes[:168]]

for a in range(-1000+1, 1000):
    for b in possible_b:
        c = check_prime_chain(a,b)
        if c > max_chain:
            max_chain = c
            max_a = a
            max_b = b
            print max_a, max_b, max_chain
print max_a * max_b
