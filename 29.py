# Distinct powers

power = [a**b for a in range(2, 101) for b in range(2, 101)]

print len(set(power))
