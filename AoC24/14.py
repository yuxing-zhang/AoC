from functools import reduce
import numpy as np
from collections import Counter


m, n = 103, 101
f = open('input')
p, v = [], []
for l in f:
    pi, vi = l.split()
    pi, vi = pi[2:], vi[2:]
    pi, vi = pi.split(','), vi.split(',')
    p.append((int(pi[0]), int(pi[1])))
    v.append((int(vi[0]), int(vi[1])))
p, v = np.array(p), np.array(v)
t = 0
for i in range(103):
    t += 1
    p += v
    x, y = p[:, 0], p[:, 1]
    x[x >= n] -= n
    x[x < 0] += n
    y[y >= m] -= m
    y[y < 0] += m
    print( Counter(x).most_common(1)[0])
g = [['.'] * 101 for _ in range(103)]
for i, j in p: g[j][i] = '#'
print('\n'.join(''.join(c for c in r) for r in g))
'''
s = [0] * 4
for x, y in p:
    if 0 <= x < n // 2:
        if 0 <= y < m // 2:
            s[0] += 1
        elif y > m // 2:
            s[2] += 1
    elif x > n // 2:
        if 0 <= y < m // 2:
            s[1] += 1
        elif y > m // 2:
            s[3] += 1
sp = s[0] * s[1] * s[2] * s[3] 
if sp > t:
    t = sp
    im = i
'''
#print(reduce(lambda x, y: x * y, s))
