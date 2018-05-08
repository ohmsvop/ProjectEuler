# Poker hands

from collections import Counter

value = [v for v in 'AKQJT98765432']
value_rank = {key: i for i, key in enumerate(value)}
straight_values = [value[i:i+5] for i in range(len(value)-4)] + [['A', '5', '4', '3', '2']]
straight_values = [set(i) for i in straight_values]

def cards_prep(cards):
    cards = cards.split()
    cards.sort(key = lambda x: value_rank[x[:-1]])
    values, suits = zip(*[(c[0], c[1]) for c in cards])
    return (values, suits)

def high_cards(cards):
    values, suits = cards_prep(cards)
    return True, list(values)

def one_pairs(cards):
    values, suits = cards_prep(cards)
    cv = Counter(values)
    v, c = zip(*cv.most_common())
    if c == (2, 1, 1, 1):
        v = list(v)
        v0, v1 = v[:1], v[1:]
        v1.sort(key = lambda x: value_rank[x])
        return True, v0 + v1
    else:
        return False, []

def two_pairs(cards):
    values, suits = cards_prep(cards)
    cv = Counter(values)
    v, c = zip(*cv.most_common())
    if c == (2, 2, 1):
        v = list(v)
        v0, v1 = v[:2], v[2:]
        v0.sort(key = lambda x: value_rank[x])
        return True, v0 + v1
    else:
        return False, []

def three_of_a_kind(cards):
    values, suits = cards_prep(cards)
    cv = Counter(values)
    v, c = zip(*cv.most_common())
    if c == (3, 1, 1):
        v = list(v)
        v0, v1 = v[:1], v[1:]
        v1.sort(key = lambda x: value_rank[x])
        return True, v0 + v1
    else:
        return False, []

def straight(cards):
    values, suits = cards_prep(cards)
    if set(values) in straight_values:
        return True, [values[0]]
    else:
        return False, []

def flush(cards):
    values, suits = cards_prep(cards)
    if len(set(suits)) == 1:
        return True, [values[0]]
    else:
        return False, []

def full_house(cards):
    values, suits = cards_prep(cards)
    cv = Counter(values)
    v, c = zip(*cv.most_common())
    if c == (3, 2):
        return True, list(v)
    else:
        return False, []

def four_of_a_kind(cards):
    values, suits = cards_prep(cards)
    cv = Counter(values)
    v, c = zip(*cv.most_common())
    if c == (4, 1):
        return True, list(v)
    else:
        return False, []

def straight_flush(cards):
    s, sc = straight(cards)
    f, _ = flush(cards)
    if s and f: 
        return True, sc
    else:
        return False, []

def royal_flush(cards):
    f, _ = flush(cards)
    if not f:
        return False, []
    else:
        values, suits = cards_prep(cards)
        if set(values) == {'T', 'J', 'Q', 'K', 'A'}:
            return True, [] 
        else:
            return False, []

def compare(p1, p2):
    p1 = match(p1)
    p2 = match(p2)
    i = 0
    while True:
        if p1[i][0] and p2[i][0]:
            for j in range(len(p1[i][1])):
                if value_rank[p1[i][1][j]] > value_rank[p2[i][1][j]]:
                    return 2
                elif value_rank[p1[i][1][j]] < value_rank[p2[i][1][j]]:
                    return 1
        elif p1[i][0]:
            return 1
        elif p2[i][0]:
            return 2
        i += 1

def match(cards):
    matched_pattern = [royal_flush(cards), straight_flush(cards), four_of_a_kind(cards),
                       full_house(cards), flush(cards), straight(cards), three_of_a_kind(cards),
                       two_pairs(cards), one_pairs(cards), high_cards(cards)]
    return matched_pattern

assert compare('5H 5C 6S 7S KD', '2C 3S 8S 8D TD') == 2
assert compare('5D 8C 9S JS AC', '2C 5C 7D 8S QH') == 1
assert compare('2D 9C AS AH AC', '3D 6D 7D TD QD') == 2
assert compare('4D 6S 9H QH QC', '3D 6D 7H QD QS') == 1
assert compare('2H 2D 4C 4D 4S', '3C 3D 3S 9S 9D') == 1

data = open('data/54.txt').read()
data = data.split("\n")[:-1]

p1_win = 0
for cards in data:
    cards = cards.split()
    c1 = " ".join(cards[:5])
    c2 = " ".join(cards[5:])
    if compare(c1, c2) == 1:
        p1_win += 1

print p1_win
