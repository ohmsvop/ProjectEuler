# Counting summations

coins = range(1, 100)

target = 100
method = [0]*(target+1)
method[0] = 1

#for coin in coins:
for coin in coins:
    for i in range(coin, target+1):
        method[i] += method[i - coin]

print method[target]
