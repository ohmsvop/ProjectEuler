# Largest product in a grid

number = open("data/11.txt").read()
number = number.split("\n")
number = [row.split() for row in number]
number = [map(int, row) for row in number]

max_multiple = 0
p = 4

m = len(number)
n = len(number[0])

# horizontal
for i in range(m):
    for j in range(n-p):
        c = 1
        for k in range(p):
            c *= number[i][j+k]
        if c > max_multiple:
            max_multiple = c

# vertical
for j in range(n):
    for i in range(m-p):
        c = 1
        for k in range(p):
            c *= number[i+k][j]
        if c > max_multiple:
            max_multiple = c

# diagonal \
for i in range(m-p):
    for j in range(n-p):
        c = 1
        for k in range(p):
            c *= number[i+k][j+k]
        if c > max_multiple:
            max_multiple = c

# diagonal /
for i in range(m-p):
    for j in range(p-1, n):
        c = 1
        for k in range(p):
            c *= number[i+k][j-k]
        if c > max_multiple:
            max_multiple = c

print max_multiple
