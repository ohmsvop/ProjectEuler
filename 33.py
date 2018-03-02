# Digit cancelling fractions

def check(n, d):
    ns = str(n)
    ds = str(d)
    if "0" in ns or "0" in ds:
        return False
    common = set(ns).intersection(set(ds))
    if not common:
        return False
    else:
        common = common.pop()
    ni = int(ns.replace(common, "", 1))
    di = int(ds.replace(common, "", 1)) 
    if n * di == d * ni:
        return True
    else:
        return False

candidate = []
for d in range(10,100):
    for n in range(10,d):
        if check(n,d):
            candidate.append((n,d))
print candidate
