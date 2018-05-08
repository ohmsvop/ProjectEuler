# XOR decryption
# TODO: need to find the key first
from itertools import product
import string

data = open("data/59.txt").read()[:-1]
data = data.split(",")
data = [int(i) for i in data]

not_allowed_ch = list('@#$%^`=+{}')

def decode(data, code):
    code = list(code)
    code = [ord(i) for i in code]
    decode_txt = []
    for i in range(len(data)):
        decode_ch = data[i] ^ code[i%3]
        if decode_ch <= 31 or chr(decode_ch) in not_allowed_ch:
            return False
        decode_txt.append(decode_ch)
    decode_txt = [chr(i) for i in decode_txt]
    decode_txt = "".join(decode_txt)
    return decode_txt

# try all possible code
codes = product(*[list(string.lowercase)]*3)
for code in codes:
    d = decode(data, code)
    if d:
        print code, d[:50]

# the code is 'god'
code = 'god'
d = decode(data, code)
print sum(ord(c) for c in d)
