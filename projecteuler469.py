# Empty chairs
from __future__ import division

linear_expectation = [0,1,1]

for i in range(3,100):
    e = 1 
    for j in range(i-1):
        e += 2/i*linear_expectation[j]
    linear_expectation.append(e)

    round_expectation = (linear_expectation[i-3]+1)/i
    print "{0:.14f}".format(1 - round_expectation)
