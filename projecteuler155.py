# Counting Capacitor Circuits
from fractions import Fraction

capacitor = Fraction(60)
n_capacitor = 18

values = dict()

def parallel(c1, c2):
    return c1*c2/(c1+c2)

def series(c1,c2):
    return c1+c2

values[1] = {capacitor}

for n in range(2, n_capacitor + 1):
    values[n] = []

    for i in range(1,n/2+1):
        for v1 in list(values[i]):
            for v2 in list(values[n-i]):
                #print n-i,i,v1,v2
                values[n].append(parallel(v1, v2))
                values[n].append(series(v1, v2))
    values[n] = set(values[n])

all_values = set()
for n in range(1,n_capacitor + 1):
    all_values = all_values.union(values[n])
    print n, len(all_values)
