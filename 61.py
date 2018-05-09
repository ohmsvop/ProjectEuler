# Cyclical figurate numbers

# step 1: generate polygonal numbers with 4-digit
# step 2: given a sequence, concatenate numbers

from itertools import permutations

formula = ['n*(n+1)/2', 'n*n', 'n*(3*n-1)/2',
           'n*(2*n-1)', 'n*(5*n-3)/2', 'n*(3*n-2)']

polygonal = {}
p = 3
for f in formula:
    n = 1
    plist = []
    while True:
        d = eval(f)
        if d >= 10000:
            break
        elif d >= 1000:
            plist.append(d) 
        n += 1
    polygonal[p] = plist
    p += 1

def concatenate(plist1, plist2):
    pc = []
    for p1 in plist1:
        for p2 in plist2:
            p1, p2 = str(p1), str(p2)
            if p1[-2:] == p2[:2]:
                pc.append(p1+p2[2:])
    return pc

for perm in permutations(range(3, 8)):
    # start and end at polygonal[8]
    pc = polygonal[8]
    n = 1
    for s in perm:
        pc = concatenate(pc, polygonal[s])
        if not pc:
            break
        n += 1
        if n == 6:
            for p in pc:
                if p[:2] == p[-2:]:
                    only_p = p

print sum(int(only_p[i:i+4]) for i in range(0,12,2))
