# Triangular, pentagonal, and hexagonal

def T():
    n = 0
    while True:
        n += 1
        yield n*(n+1)/2

def P():
    n = 0
    while True:
        n += 1
        yield n*(3*n-1)/2

def H():
    n = 0
    while True:
        n += 1
        yield n*(2*n-1)

tg, pg, hg = T(), P(), H()
t, p, h = tg.next(), pg.next(), hg.next()
candidate = []

n = 0
while True:
    if t < p:
        t = tg.next()
    elif p < t:
        p = pg.next()
    elif p < h:
        p = pg.next()
    elif h < p:
        h = hg.next()
    else:    
        n += 1
        candidate.append(t)
        if n == 3:
            break
        else:
            t = tg.next()

print candidate[-1]
