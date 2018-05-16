# Large non-Mersenne prime

# 28433*2**7830457+1

n = 2 ** 7830457 % 10 ** 10
n = 28433 * n + 1
n %= 10 ** 10
print n
