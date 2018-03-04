# Pentagon numbers

limit = 10000
pentagon = [n*(3*n-1)/2 for n in range(limit)]
pentagon_set = set(pentagon)

def check(p1, p2):
    if p1 + p2 not in pentagon_set:
        return False
    if p1 - p2 not in pentagon_set:
        return False
    return True

candidate = []
for i1 in range(1,limit):
    for i2 in range(1,i1):
        p1 = pentagon[i1]
        p2 = pentagon[i2]
        if check(p1, p2):
            candidate.append((i1, i2, p1,p2,p1-p2))

