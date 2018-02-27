# Multiples of 3 and 5

limit = 1000

i3 = [i for i in range(3, limit, 3)]
i5 = [i for i in range(5, limit, 5)]
i15 = [i for i in range(15, limit, 15)]

sum_3_5 = sum(i3) + sum(i5) - sum(i15)
print sum_3_5
