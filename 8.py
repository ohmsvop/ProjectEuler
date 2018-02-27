# Largest product in a series

digit = open("data/8.txt").read()
digit = "".join(digit.split())
digit = list(int(d) for d in digit)

digit_multiply = digit[:] 
for j in range(1,13): 
    digit_multiply = [digit_multiply[i] * digit[i+j] for i in range(len(digit_multiply)-j)]

print max(digit_multiply)
