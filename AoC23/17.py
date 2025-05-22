from collections import defaultdict as dd
from itertools import product

f = open('input')
data = [[int(x) for x in l[:-1]] for l in f]
f.close()

m, n = len(data), len(data[0])
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class H():
    def __init__(self, g):
        self.t = list(g)
        self.d = {k: v for v, k in enumerate(self.t)}
        self.v = {k: float('inf') for k in self.t}
    def __len__(self):
        return len(self.t)
    def _swap(self, i, j):
        self.t[i], self.t[j] = self.t[j], self.t[i]
        self.d[self.t[i]], self.d[self.t[j]] = i, j
    def pop(self):
        if not self.t:
            return
        x = self.t[0]
        if len(self.t) == 1:
            return self.t.pop(), self.v[x]
        self.t[0] = self.t.pop()
        i, j = 0, 1
        while j < len(self.t):
            if j + 1 < len(self.t) and self.v[self.t[j + 1]] <\
                    self.v[self.t[j]]:
                j += 1
            if self.v[self.t[j]] >= self.v[self.t[i]]:
                break
            self._swap(i, j)
            i, j = j, 2 * j + 1
        return x, self.v[x]
    def update(self, k, v):
        if self.v[k] > v:
            self.v[k] = v
            i = self.d[k]
            while i:
                j = (i - 1) // 2
                if self.v[self.t[j]] <= self.v[self.t[i]]:
                    break
                self._swap(i, j)
                i = j

# part 1
c = [1, 2, 3]
g = dd(list)
for i, j, k, l in product(range(m), range(n), d, c):
    if l < 3:
        i_, j_ = i + k[0], j + k[1]
        if 0 <= i_ < m and 0 <= j_ < n:
            g[(i, j, k, l)].append((i_, j_, k, l + 1, data[i_][j_]))
    s = [(0, 1), (0, -1)] if k[1] == 0 else [(1, 0), (-1, 0)]
    for u in s:
        i_, j_ = i + u[0], j + u[1]
        if 0 <= i_ < m and 0 <= j_ < n:
            g[(i, j, k, l)].append((i_, j_, u, 1, data[i_][j_]))
g[(0, 0, None, 0)].append((0, 1, (0, 1), 1, data[0][1]))
g[(0, 0, None, 0)].append((1, 0, (1, 0), 1, data[1][0]))

h = H(g)
h.update((0, 0, None, 0), 0)
visited = set()
s = float('inf')
while len(h):
    k, v = h.pop()
    visited.add(k)
    if k[:2] == (m - 1, n - 1):
        s = min(s, v)
    if v == float('inf'):
        break
    for j in g[k]:
        h.update(j[:-1], v + j[-1])
print(s)

# part 2
g = {}
for i, j, k, l in product(range(m), range(n), d, range(1, 11)):
    g[(i, j, k, l)] = []
    if l < 10:
        i_, j_ = i + k[0], j + k[1]
        if 0 <= i_ < m and 0 <= j_ < n:
            g[(i, j, k, l)].append((i_, j_, k, l + 1, data[i_][j_]))
    if l >= 4:
        s = [(0, 1), (0, -1)] if k[1] == 0 else [(1, 0), (-1, 0)]
        for u in s:
            i_, j_ = i + u[0], j + u[1]
            if 0 <= i_ < m and 0 <= j_ < n:
                g[(i, j, k, l)].append((i_, j_, u, 1, data[i_][j_]))
g[(0, 0, None, 0)] = []
g[(0, 0, None, 0)].append((0, 1, (0, 1), 1, data[0][1]))
g[(0, 0, None, 0)].append((1, 0, (1, 0), 1, data[1][0]))

h = H(g)
h.update((0, 0, None, 0), 0)
visited = set()
s = float('inf')
while len(h):
    k, v = h.pop()
    visited.add(k)
    if k[:2] == (m - 1, n - 1) and k[-1] >= 4:
        s = min(s, v)
    if v == float('inf'):
        break
    for j in g[k]:
        h.update(j[:-1], v + j[-1])
print(s)
