# Longest Collatz sequence

limit = 1000000

def collatz(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        length += 1
    return length

max_length = 0
for i in range(1, limit+1):
    l = collatz(i)
    if l > max_length:
        print l, i
        max_length = l
