from collections import Counter
from functools import cmp_to_key

f = open('input')
h = []
for l in f:
    t = l.split()
    h.append((t[0], int(t[1])))
f.close()

# part 1
def cmp(s, t):
    s, t = s[0], t[0]
    d = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6,
         '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}
    sc = sorted(Counter(s).values(), reverse=True)
    tc = sorted(Counter(t).values(), reverse=True)
    if sc > tc: return 1
    if sc < tc: return -1
    for i, j in zip(s, t):
        if d[i] > d[j]: return 1
        if d[i] < d[j]: return -1

s = 0
for i, x in enumerate(sorted(h, key=cmp_to_key(cmp)), 1):
    s += i * x[1]
print(s)

# part 2
def cmp(s, t):
    s, t = s[0], t[0]
    d = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6,
         '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0, 'J': -1}
    sc, tc = Counter(s), Counter(t)
    sj, tj = sc['J'], tc['J']
    del sc['J']
    del tc['J']
    sc = sorted(sc.values(), reverse=True)
    if not sc: sc = [0]
    sc[0] += sj
    tc = sorted(tc.values(), reverse=True)
    if not tc: tc = [0]
    tc[0] += tj
    if sc > tc: return 1
    if sc < tc: return -1
    for i, j in zip(s, t):
        if d[i] > d[j]: return 1
        if d[i] < d[j]: return -1

s = 0
for i, x in enumerate(sorted(h, key=cmp_to_key(cmp)), 1):
    s += i * x[1]
print(s)
