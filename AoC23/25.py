from collections import defaultdict as dd

def sw(g):
    cmin = float('inf')
    n = {k: (k,) for k in g.keys()}
    while len(g) > 1:
        h = H(g.keys())
        a = next(iter(g.keys()))
        h.inc(a, 1)
        s = set()
        p, u = None, None
        while len(h) > 0:
            p = u
            u, c = h.pop()
            s.add(u)
            for v, w in g[u].items():
                if v not in s:
                    h.inc(v, w)
        if c < cmin:
            cmin = c
            tmin = n[u]
        n[p] += n[u]
        for v, w in g[u].items():
            if v != p:
                g[p][v] += w
                g[v][p] += w
        for v in g[u]:
            del g[v][u]
        del g[u]
    return cmin, tmin

class H():
    def __init__(self, s):
        self.t = [[x, 0] for x in s]
        self.i = {x: i for (i, x) in enumerate(s)}
    def __len__(self):
        return len(self.t)
    def _swap(self, i, j):
        x, y = self.t[i][0], self.t[j][0]
        self.i[x], self.i[y] = j, i
        self.t[i], self.t[j] = self.t[j], self.t[i]
    def pop(self):
        n = len(self.t)
        if n == 0: return
        if n == 1:
            return self.t.pop()
        x = self.t[0]
        self.t[0] = self.t.pop()
        self.i[self.t[0][0]] = 0
        i, j = 0, 1
        while j < len(self.t):
            if j + 1 < len(self.t) and self.t[j + 1][1] > self.t[j][1]:
                j += 1
            if self.t[i][1] >= self.t[j][1]:
                break
            self._swap(i, j)
            i, j = j, 2 * j + 1
        return x
    def inc(self, k, v):
        i = self.i[k]
        self.t[i][1] += v
        j = (i - 1) // 2
        while i > 0:
            if self.t[j][1] >= self.t[i][1]:
                break
            self._swap(i, j)
            i, j = j, (j - 1) // 2

g = dd(lambda : dd(int))
f = open('input')
for l in f:
    l_ = l.split()
    u = l_[0][:-1]
    for v in l_[1:]:
        g[u][v] = g[v][u] = 1
f.close()
n = len(g)
c, t = sw(g)
print(c, len(t) * (n - len(t)))
