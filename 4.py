# Largest palindrome product

def check_palindrome(n):
    n = str(n)
    half_length = len(n)/2
    for i in range(half_length):
        if n[i] != n[-i-1]:
            return False
    return True

max_palindrome = 0
for i in range(999,99,-1):
    for j in range(999,99,-1):
        n = i*j
        if n > max_palindrome and check_palindrome(n):
            max_palindrome = n

print max_palindrome
