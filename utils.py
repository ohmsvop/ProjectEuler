from collections import Counter 
from math import factorial

def sieve(n):
    "Return all primes <= n."
    primes = list(range(n + 1))
    primes[1] = 0
    sqrtn = int(round(n ** 0.5))
    for i in range(2, sqrtn + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = 0
    return filter(None, primes)

def is_prime(n):
    # fermat
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # a**(p-1) = 1 (mod p) if a, p coprime
    return pow(2, n-1, n) == 1

def is_square(n):
    if int(n**0.5)**2 == n:
        return True
    else:
        return False

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a,b):
    r = gcd(a,b)
    return a*b/r

def prime_factorization(n):
    if n == 1:
        return Counter()
    primes = sieve(int(n))
    p_index = 0
    n_factor = []
    while True:
        p = primes[p_index]
        if n < p:
            break
        elif n % p == 0:
            n /= p
            n_factor.append(p)
        else:
            p_index += 1
    c = Counter(n_factor)
    return c

def sum_proper_divisor(n):
    pf = prime_factorization(n)
    sum_d = 1
    for p in pf:
        d = 0
        for i in range(pf[p]+1):
            d += p**i
        sum_d *= d
    sum_d -= n
    return sum_d

def P(n, r):
    return factorial(n)/factorial(n-r)

def C(n, r):
    return factorial(n)/factorial(r)/factorial(n-r)

def continued_fraction(n):
    m = 0
    d = 1
    a = a0 = int(n**0.5)
    expansion = [a0]
    while a != 2*a0:
        m = d*a-m
        d = (n-m**2)/d
        a = (a0+m)/d
        expansion.append(a)
    return expansion
