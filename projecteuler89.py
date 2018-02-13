f = open("roman.txt")
saved = 0
for l in f.readlines():
    if "DCCCC" in l:
        saved +=3
    elif "CCCC" in l:
        saved +=2
    if "LXXXX" in l:
        saved +=3
    elif "XXXX" in l:
        saved +=2
    if "VIIII" in l:
        saved +=3
    elif "IIII" in l:
        saved +=2  
print saved
