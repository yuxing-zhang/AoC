from collections import Counter
from functools import reduce

def check(game, config):
# check if game is possible with the configuration
    for color, count in game.items():
        if count > config[color]:
            return False
    return True

def parse(s):
# parse a string into a game
    d = Counter()
    s = s.split()
    for i, j in zip(s[::2], s[1::2]):
        d[j[:-1]] = int(i)
    return d

# part 1
f = open('input')
s = 0
config = Counter({'red': 12, 'green': 13, 'blue': 14})
for l in f:
    k = l.find(':')
    i = k + 2
    # replace \n with ;
    l = l[:-1] + ';'
    while True:
        j = l.find(';', i)
        if j == -1: break
        g = parse(l[i:j+1])
        if not check(g, config): break
        i = j + 2
    if j == -1:
        s += int(l[5:k])
print(s)
f.close()

# part 2
f = open('input')
s = 0
for l in f:
    i = l.find(':') + 2
    l = l[:-1] + ';'
    g = Counter()
    while True:
        j = l.find(';', i)
        if j == -1: break
        for c, n in parse(l[i:j+1]).items():
            g[c] = max(g[c], n)
        i = j + 2
    s += reduce(lambda x, y: x * y, g.values())
print(s)
f.close()
