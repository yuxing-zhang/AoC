import numpy as np

class H():
    def __init__(self, m, n):
        self.t = [(i, j) for i in range(m) for j in range(n)]
        self.v = [[float('inf')] * n for _ in range(m)]
        self.v[0][0] = 0
        self.i = [list(range(i * n, i * n + n)) for i in range(m)]

    def pop(self):
        if len(self.t) == 1:
            return self.t.pop()
        x = self.t[0]
        self.t[0] = self.t.pop()
#        ii, ij = self.t[0]
#        self.i[ii][ij] = 0
        i = 0
        while 2 * i + 1 < len(self.t):
            ii, ij = self.t[i]
            j = 2 * i + 1
            ji, jj = self.t[j]
            if 2 * i + 2 < len(self.t):
                ki, kj = self.t[2 * i + 2]
                if self.v[ki][kj] < self.v[ji][jj]:
                    j += 1
                    ji, jj = ki, kj
            if self.v[ji][jj] >= self.v[ii][ij]:
                break
            self.t[i], self.t[j] = self.t[j], self.t[i]
            self.i[ii][ij] = j
            self.i[ji][jj] = i
            i = j
        return x

    def upd(self, xi, xj, v):
        if v >= self.v[xi][xj]: return
        self.v[xi][xj] = v
        i = self.i[xi][xj]
        while i:
            j = (i - 1) // 2
            ii, ij = self.t[i]
            ji, jj = self.t[j]
            if self.v[ji][jj] <= self.v[ii][ij]:
                break
            self.t[i], self.t[j] = self.t[j], self.t[i]
            self.i[ii][ij] = j
            self.i[ji][jj] = i
            i = j

f = open('input')
g = np.array([[int(x) for x in r[:-1]] for r in f])
m, n = len(g), len(g[0])
h = H(m, n)

g5 = g + np.arange(5)[:, None, None] + np.arange(5)[:, None, None, None]
g5 %= 9
g5[g5 == 0] += 9
g5 = g5.swapaxes(1, 2).reshape(5 * m, -1)
m5, n5 = m * 5, n * 5
h5 = H(m5, n5)
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while True:
    i, j = h.pop()
    if i == m - 1 and j == n - 1:
        print(h.v[i][j])
        break
    for di, dj in d:
        i_, j_ = i + di, j + dj
        if 0 <= i_ < m and 0 <= j_ < n:
            h.upd(i_, j_, h.v[i][j] + g[i_][j_])
while True:
    i, j = h5.pop()
    if i == m5 - 1 and j == n5 - 1:
        print(h5.v[i][j])
        break
    for di, dj in d:
        i_, j_ = i + di, j + dj
        if 0 <= i_ < m5 and 0 <= j_ < n5:
            h5.upd(i_, j_, h5.v[i][j] + g5[i_][j_])
     
