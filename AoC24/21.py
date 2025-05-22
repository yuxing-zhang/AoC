from itertools import product
from collections import defaultdict as DD

def vst(i, j, d, s, dd, ds, pad):
    m, n = len(pad), len(pad[0])
    vstd.add((i, j))
    if not (i, j) in dd or d < dd[(i, j)]:
        ds[(i, j)] = {s}
        dd[(i, j)] = d
    elif d == dd[(i, j)]:
        ds[(i, j)].add(s)
    for (di, dj), s_ in zip([(-1, 0), (0, 1), (1, 0), (0, -1)], '^>v<'):
        i_, j_ = i + di, j + dj
        if 0 <= i_ < m and 0 <= j_ < n and pad[i_][j_] != 'x' and\
                not (i_, j_) in vstd:
            vst(i_, j_, d + 1, s + s_, dd, ds, pad)
    vstd.remove((i, j))

nup = ['789', '456', '123', 'x0A']
dip = ['x^A', '<v>']
pads = [nup, dip]
d = [{}, {}]
for k in range(2):
    m, n = len(pads[k]), len(pads[k][0])
    for i in range(m):
        for j in range(n):
            if pads[k][i][j] != 'x':
                dd, ds = {}, {}
                vstd = set()
                vst(i, j, 0, '', dd, ds, pads[k])
                for i_ in range(m):
                    for j_ in range(n):
                        if pads[k][i_][j_] != 'x':
                            d[k][(pads[k][i][j], pads[k][i_][j_])] =\
                                    [s + 'A' for s in ds[(i_, j_)]]

c = [{} for _ in range(26)]
c[0] = DD(lambda : 1)
for i in range(25):
    for u in '<^>vA':
        for v in '<^>vA':
            c[i + 1][(u, v)] = min(sum(c[i][(x, y)] for x, y in\
                    zip('A' + p, p)) for p in d[1][(u, v)])

def check(s, n):
    if n == 0:
        return len(s)
    s = 'A' + s
    return min(check(''.join(p), n - 1) for p in\
            product(*[d[1][(x, y)] for x, y in zip(s, s[1:])]))

def check(s, n):
    return sum(c[n][(x, y)] for x, y in zip('A' + s, s))

f = open('input')
s = 0
for l in f:
    l = l[:-1]
    s += int(l[:-1]) * min(check(''.join(p), 25) for p in\
            product(*(d[0][(x, y)] for x, y in zip('A' + l, l))))
print(s)
