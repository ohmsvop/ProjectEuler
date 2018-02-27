from utils import sieve
from math import log, sqrt
import time

N = 10000000
primes = sieve(N/2)

def M(p1, p2, N):
    N1 = int(log(N, p1))
    N2 = int(log(N, p2))
    candidate = [p1**i * p2**j for i in range(1,N1+1) for j in range(1,N2+1)]
    max_candidate = 0
    for c in candidate:
        if c <= N and c > max_candidate:
            max_candidate = c
    return max_candidate

start = time.time()
sum_M = 0
max_i = sqrt(N)
for i in primes:
    if i <= max_i:
        max_j = N/i
        for j in primes:
            if j <= max_j and j > i:
                m = M(i,j,N)
                sum_M += m
end = time.time()

print sum_M
print "Spent time: {}s".format(end - start)
