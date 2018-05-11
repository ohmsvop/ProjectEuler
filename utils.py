from collections import Counter 
from math import factorial

def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = range(np1)
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in xrange(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(xrange(i*i, np1, i))
    return filter(None, s)

def is_prime(n):
    # fermat
    if n == 2:
        return True
    if not n & 1:
        return False
    return pow(2, n-1, n) == 1

def is_square(n):
    if int(n**0.5)**2 == n:
        return True
    else:
        return False

def gcd(a,b):
    assert type(a) == int
    assert type(b) == int
    if a < b:
        a, b = b, a
    while True:
        r = a % b
        if r == 0:
            break
        else:
            a, b = b, r
    return b

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
