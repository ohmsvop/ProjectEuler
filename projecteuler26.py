# Reciprocal cycles

def find_cycle_length(d):
    r = 1
    residual = [r]
    while True:
        r = r*10 % d
        if r in residual:
            start = residual.index(r)
            n = len(residual[start:])
            break
        if r == 0:
            n = 0
            break
        residual.append(r)
    return n 

max_n = 0
max_d = 0
for d in range(2,1000):
    n = find_cycle_length(d)
    if n > max_n:
        max_n = n
        max_d = d
print "{} has cycle_length {}".format(max_d, max_n)
