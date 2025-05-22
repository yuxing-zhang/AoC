from collections import defaultdict as DD
from functools import reduce

f = open('input')
mat = [list(l)[:-1] for l in f]
m, n = len(mat), len(mat[0])
mat[-2][1] = mat[1][-2] = '.'
d = {}
for i in range(1, m - 1):
    j1 = 1
    while True:
        j0 = j1
        while j0 < n - 1 and mat[i][j0] == '#':
            j0 += 1
        if j0 == n - 1:
            break
        j1 = j0 + 1
        while mat[i - 1][j1] == mat[i + 1][j1] == '#' and mat[i][j1] == '.':
            j1 += 1
        if mat[i][j1] == '.':
            d[(i, j0, 0, 1)] = (i, j1, 0, 1, j1 - j0)
            d[(i, j1, 0, -1)] = (i, j0, 0, -1, j1 - j0)
        elif j1 - j0 > 1:
            d[(i, j0, 0, 1)] = (i, j1 - 1, 0, 1, j1 - j0 - 1)
            d[(i, j1 - 1, 0, -1)] = (i, j0, 0, -1, j1 - j0 - 1)

for j in range(1, n - 1):
    i1 = 1
    while True:
        i0 = i1
        while i0 < m - 1 and mat[i0][j] == '#':
            i0 += 1
        if i0 == m - 1:
            break
        i1 = i0 + 1
        while mat[i1][j - 1] == mat[i1][j + 1] == '#' and mat[i1][j] == '.':
            i1 += 1
        if mat[i1][j] == '.':
            d[(i0, j, 1, 0)] = (i1, j, 1, 0, i1 - i0)
            d[(i1, j, -1, 0)] = (i0, j, -1, 0, i1 - i0)
        elif i1 - i0 > 1:
            d[(i0, j, 1, 0)] = (i1 - 1, j, 1, 0, i1 - i0 - 1)
            d[(i1 - 1, j, -1, 0)] = (i0, j, -1, 0, i1 - i0 - 1)

g = DD(set)
for u, v in d.items():
    g[u].add(v)
    i, j, di, dj, _ = v
    if mat[i + dj][j + di] == '.':
        g[v[:-1]].add((i, j, dj, di, 1000))
    if mat[i - dj][j - di] == '.':
        g[v[:-1]].add((i, j, -dj, -di, 1000))
if mat[-3][1] == '.':
    g[(m - 2, 1, 0, 1)].add((m - 2, 1, -1, 0, 1000))

class H():
    def __init__(self, g):
        self.t = []
        self.i = {}
        for u in g:
            if not u in self.i:
                self._add(u)
            for v in g[u]:
                if not v[:-1] in self.i:
                    self._add(v[:-1])

    def _add(self, u):
        self.i[u] = len(self.t)
        self.t.append([u, float('inf')])

    def pop(self):
        del  self.i[self.t[0][0]]
        if len(self.t) == 1:
            return self.t.pop()
        x = self.t[0]
        self.t[0] = self.t.pop()
        self.i[self.t[0][0]] = 0
        i, j = 0, 1
        while j < len(self.t):
            if j + 1 < len(self.t) and self.t[j + 1][1] < self.t[j][1]:
                j += 1
            if self.t[j][1] >= self.t[i][1]:
                break
            self.t[i], self.t[j] = self.t[j], self.t[i]
            self.i[self.t[i][0]], self.i[self.t[j][0]] = i, j
            i, j = j, 2 * j + 1
        return x
    
    def update(self, v, u, n):
        if p[u][0] == n:
            p[u][1].add(v)
        elif p[u][0] > n:
            p[u] = [n, {v}]
        if u not in self.i:
            return
        i = self.i[u]
        if self.t[i][1] <= n: return
        self.t[i][1] = n
        while i > 0:
            j = (i - 1) // 2
            if self.t[j][1] <= self.t[i][1]:
                break
            self.t[i], self.t[j] = self.t[j], self.t[i]
            self.i[self.t[i][0]], self.i[self.t[j][0]] = i, j
            i = j

h = H(g)
p = DD(lambda : [float('inf'), set()])
h.update((m - 2, 1, 0, 1), (m - 2, 1, 0, 1), 0)
p[(m - 2, 1, 0, 1)][1] = set()
while h.t:
    u = h.pop()
    for v in g[u[0]]:
        h.update(u[0], v[:-1], u[-1] + v[-1])

def s(u):
    r = {u[:2]}
    if not p[u][1]: return r
    for v in p[u][1]:
        if v[2:] == u[2:]:
            i, j, di, dj = u
            while (i - di, j - dj, di, dj) != v:
                i, j = i - di, j - dj
                r.add((i, j))
        r |= s(v)
    return r
print(len(s((1, n - 2, 0, 1))))
