# Self powers

def self_power(n):
    return str(n**n)[-10:]

total = sum(int(self_power(i)) for i in range(1, 1001))
print str(total)[-10:]
