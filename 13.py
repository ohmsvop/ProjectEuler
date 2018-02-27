
digits = open("data/13.txt").read()
digits = digits.split()
digits = [int(d) for d in digits]
s = sum(digits)
print str(s)[:10]
