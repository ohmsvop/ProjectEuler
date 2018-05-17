# Coin partitions
# p[n] = p[n-1] + p[n-2] - p[n-5] - p[n-7] + p[n-12] ...

def pentagonal(n):
    return n*(3*n-1)/2

def generate_sign():
    while True:
        yield 1
        yield 1
        yield -1
        yield -1

def generate_seq():
    n = 1
    while True:
        yield pentagonal(n)
        yield pentagonal(-n)
        n += 1

seq = generate_seq()
seq = [seq.next() for i in range(1000)]

p = [1]
n = 1
while True:
    sum_p = 0
    sign = generate_sign()
    for k in seq:
        s = sign.next()
        if n - k >= 0:
            sum_p += p[n - k] * s
        else:
            break
    sum_p %= 10**6
    p.append(sum_p)
    if sum_p == 0:
        break
    n += 1
print n
