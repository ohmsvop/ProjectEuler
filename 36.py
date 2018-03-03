# Double-base palindromes

def check_palindrome(n):
    n = str(n)
    half_length = len(n)/2
    for i in range(half_length):
        if n[i] != n[-i-1]:
            return False
    return True

limit = 1000000

candidate = []
for i in range(1, limit):
    if check_palindrome(i) and check_palindrome(bin(i)[2:]):
        candidate.append(i)

print sum(candidate)
