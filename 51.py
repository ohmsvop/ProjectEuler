from utils import sieve
from itertools import permutations, product
import re

primes = sieve(1000000)

def generate_number(template):
    a = re.sub("\*","0",template)
    b = re.sub("\d*(.*)","\\1",template)
    b = re.sub("\d","0",b)
    b = re.sub("\*","1",b)
    # return a,b
    a, b = int(a), int(b)
    number = [a+b*n for n in range(10)]
    if template[0] == "*":
        number = number[1:]
    return number

def count_primes(number):
    np = 0
    for n in number:
        if n in primes:
            np += 1
    return np

def generate_template(nstar, ndigit):
    templates = []
    star = ["*"] * nstar
    digit = product(*[[str(s) for s in range(10)]]*ndigit)
    for d in digit:
        star_digit = star[:]
        star_digit.extend(d)
        template = set(permutations(star_digit))
        templates.extend(["".join(t) for t in template])
    templates = list(sorted(set(templates)))
    return templates

#template = "56**3"
templates = generate_template(3,3)
templates = [t for t in templates if t[0] != '0']
templates = [t for t in templates if t[-1] not in ['0','2','4','5','6','8']]
for t in templates:
    number = generate_number(t)
    np = count_primes(number)
    if np > 5:
        print t, np
    if np == 8:
        break
