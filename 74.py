# Digit factorial chains

from math import factorial

def digit_factorial(n):
    digits = [int(s) for s in str(n)]
    sum_factorial = sum(factorial(d) for d in digits)
    return sum_factorial

def chain_length(n):
    length = 0
    while True:
        if n not in chain.keys():
            n = digit_factorial(n)
            length += 1
        else:
            count = chain[n]
            length += count
            break
    return length

chain = {1:1, 2:1, 145:1, 
        169:3, 363601:3, 1454:3, 
        871:2, 872:2, 
        45361:2, 45362:2,
        40585:1}

l60 = 0
for i in range(1,1000000):
    l = chain_length(i)
    if l == 60:
        l60 += 1
print l60
