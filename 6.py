# Sum square difference
limit = 100
square_of_sums = sum(i for i in range(limit+1))**2
sum_of_squares = sum(i**2 for i in range (limit+1))

print square_of_sums - sum_of_squares
