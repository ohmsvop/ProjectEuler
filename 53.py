# Combinatoric selections

from utils import C

limit = 1000000

candidate = [] 
for n in range(1, 101):
    for r in range(1, n):
        if C(n, r) > limit:
            candidate.append((n,r))

print len(candidate)
