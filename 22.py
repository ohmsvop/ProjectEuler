# Names scores
import string

names = open("data/22.txt").read()
names = names.split(",")
names = [n[1:-1] for n in names]
names.sort()
letters = string.uppercase

def name_value(name):
    value = 0
    for s in name:
        value += letters.index(s) + 1
    return value

sum_values = 0
for name in names:
    sum_values += name_value(name) * (names.index(name)+1)

print sum_values
