# Coded triangle numbers

import string

words = open("data/42.txt").read()
words = words.split(",")
words = [w.strip("\"") for w in words]

limit = max(map(len, words)) * 26

triangle = [i*(i+1)/2 for i in range(1, 30)]
triangle_set = set(triangle)

d = {x:i+1 for i,x in enumerate(string.uppercase)}

def check(word):
   word_sum = sum(d[w] for w in word)
   if word_sum in triangle_set:
       return True
   else:
       return False

candidate = [word for word in words if check(word)]
print len(candidate)
