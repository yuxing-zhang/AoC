import sys
from collections import Counter, defaultdict as DD
sys. setrecursionlimit(10000)

def vst(i, j, dist, chtd):
    if mat[i][j] == 'E':
        if not chtd:
            global d0
            d0 = dist
        else:
            dc[dist] += 1
        return    
    vstd.add((i, j))
    for di, dj in d:
        i_, j_ = i + di, j + dj
        if 0 <= i_ < m and 0 <= j_ < n and not (i_, j_) in vstd:
            if mat[i_][j_] != '#':
                vst(i_, j_, dist + 1, chtd)
            else:
                i__, j__ = i_ + di, j_ + dj
                if not chtd and 0 <= i__ < m and 0 <= j__ < n and\
                        mat[i__][j__] != '#' and not (i__, j__) in vstd:
                    vst(i__, j__, dist + 2, True)
    vstd.remove((i, j))

f = open('input')
mat = [l[:-1] for l in f]
m, n = len(mat), len(mat[0])
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
sf, ef = False, False
for i, l in enumerate(mat):
    for j, x in enumerate(l):
        if x == 'S':
            si, sj = i, j
            sf = True
        elif x == 'E':
            ei, ej = i, j
            ef = True
    if sf and ef:
        break
'''
vstd = set()
dc = Counter()
vst(si, sj, 0, False)
dc = {d0 - k: v for k, v in dc.items()}
print(sum(v for k, v in dc.items() if k >= 100))
'''

def vst(i, j, l, dist, dest):
    if l < dist[(i, j)]:
        dist[(i, j)] = l
    if mat[i][j] == dest:
        return
    vstd.add((i, j))
    for di, dj in d:
        i_, j_ = i + di, j + dj
        if 0 <= i_ < m and 0 <= j_ < n and mat[i_][j_] != '#'\
                and not (i_, j_) in vstd:
            vst(i_, j_, l + 1, dist, dest)
    vstd.remove((i, j))

sd, ed = DD(lambda : float('inf')), DD(lambda : float('inf'))
vstd = set()
vst(si, sj, 0, sd, 'E')
vstd = set()
vst(ei, ej, 0, ed, 'S')
d0 = sd[(ei, ej)]

c = Counter()
for xi in range(1, m - 1):
    for xj in range(1, n - 1):
        if mat[xi][xj] != '#':
            for yi in range(1, m - 1):
                for yj in range(1, n - 1):
                    xy = abs(xi - yi) + abs(xj - yj)
                    if mat[yi][yj] != '#' and xy <= 20:
                        se = sd[(xi, xj)] + xy + ed[(yi, yj)]
                        if se < d0:
                            c[d0 - se] += 1
print(sum(v for k, v in c.items() if k >= 100))
