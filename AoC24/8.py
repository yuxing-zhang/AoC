from collections import defaultdict
from itertools import combinations

f = open('input_')
d = defaultdict(set)
a = set()
m = 0
for i, l in enumerate(f):
    for j, c in enumerate(l):
        if c != '.' and c != '\n':
            d[c].add((i, j))
            a.add((i, j))
    m += 1
n = len(l) - 1

b = set()
for k in d:
    for i, j in combinations(d[k], 2):
        i_ = (2 * i[0] - j[0], 2 * i[1] - j[1])
        j_ = (2 * j[0] - i[0], 2 * j[1] - i[1])
        if 0 <= i_[0] < m and 0 <= i_[1] < n: b.add(i_)
        if 0 <= j_[0] < m and 0 <= j_[1] < n: b.add(j_)
print(len(b))

c = set(a)
for k in d:
    for (ix, iy), (jx, jy) in combinations(d[k], 2):
        dx, dy = ix - jx, iy - jy
        while 0 <= ix + dx < m and 0 <= iy + dy < n:
            ix, iy = ix + dx, iy + dy
            c.add((ix, iy))
        while 0 <= jx - dx < m and 0 <= jy - dy < n:
            jx, jy = jx - dx, jy - dy
            c.add((jx, jy))
print(len(c))
