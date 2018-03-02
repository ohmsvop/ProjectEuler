# Coin sums
import numpy as np

coins = [1, 2, 5, 10, 20, 50, 100, 200]

target = 200
method = [0]*(target+1)
method[0] = 1

#for coin in coins:
for coin in coins:
    for i in range(coin, target+1):
        method[i] += method[i - coin]

print method[target]
