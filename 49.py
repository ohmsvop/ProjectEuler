# Prime permutations

from utils import sieve

primes = sieve(10000)
primes = [p for p in primes if p > 1000]
primes_set = set(primes)

def check_permutation(p1, p2, p3):
    p1, p2, p3 = map(str, [p1, p2, p3])
    p1, p2, p3 = map(set, [p1, p2, p3])
    if p1 != p2:
        return False
    if p2 != p3:
        return False
    return True

for pi1 in range(len(primes)):
    for pi2 in range(pi1+1, len(primes)):
        p1 = primes[pi1]
        p2 = primes[pi2]       
        p3 =  2*p2 - p1 
        if p3 in primes_set and check_permutation(p1, p2, p3):
            print p1, p2, p3, str(p1)+str(p2)+str(p3)

    
