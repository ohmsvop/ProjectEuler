# Lychrel numbers

max_iteration = 50

def reverse(n):
    n = str(n)
    n = [i for i in n]
    n.reverse()
    n = "".join(n)
    return int(n)

def palindrome(n):
    n = str(n)
    for i in range(len(n)/2):
        if n[i] != n[-i-1]:
            return False
    return True

lychrel = []
not_lychrel = []
for n in range(1, 10001):
    init_n = n
    iter = 1
    while iter <= max_iteration:
        n += reverse(n)
        if palindrome(n):
            not_lychrel.append((init_n, iter))
            break
        if iter == max_iteration:
            lychrel.append((init_n, n, iter))
        iter += 1

print len(lychrel)
