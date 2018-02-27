f = open("roman.txt")
saved = 0
for l in f.readlines():
    # DCCCC -> CM, CCCC -> CD
    if "DCCCC" in l:
        saved += 3
    elif "CCCC" in l:
        saved += 2
    # LXXXX -> XC, XXXX -> XL    
    if "LXXXX" in l:
        saved += 3
    elif "XXXX" in l:
        saved += 2
    # VIIII -> IX, IIII -> IV
    if "VIIII" in l:
        saved += 3
    elif "IIII" in l:
        saved += 2
print saved
