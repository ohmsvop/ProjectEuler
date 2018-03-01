from collections import Counter 

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
