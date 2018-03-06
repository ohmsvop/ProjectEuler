# Distinct primes factors
from utils import prime_factorization

def factor_number(n):
    f = [0] * (n+1)
    for i in range(2,n+1):
        if f[i] == 0:
            f[i::i] = [x+1 for x in f[i::i]]
    return f    

f = factor_number(200000)
chain = 1
l = 4
for i in range(len(f)-1):
    if f[i+1] == f[i] and f[i] == l:
        chain += 1
    else:
        chain = 1
    if chain == l:
        print i - l + 2
