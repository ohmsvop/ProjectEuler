# Lattice paths
from math import factorial

n = 20
grid = [[1]*n]

for i in range(1, n+1):
    grid.append([1])
    for j in range(1, n+1):
        grid[i].append(grid[i][j-1] + grid[i-1][j])

print grid[-1][-1]

# alternative: simply by combinatorics
# 20 rights and 20 down permutation
# C(40,20)

print factorial(2*n)/factorial(n)/factorial(n)
 
