import numpy as np
from collections import deque

def flash(i, j):
    if (i, j) in flashed:
        return
    flashed.add((i, j))
    for di, dj in d:
        i_, j_ = i + di, j + dj
        if 0 <= i_ < m and 0 <= j_ < n:
            g[i_, j_] += 1
            if g[i_, j_] > 9: flash(i_, j_)

f = open('input')
g = np.array([[int(x) for x in l[:-1]] for l in f])
g2 = g.copy()
m, n = len(g), len(g[0])
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
c = 0

# DFS
for k in range(100):
    g += 1
    flashed = set()
    for i in range(m):
        for j in range(n):
            if g[i, j] > 9: flash(i, j)
    g[g > 9] = 0
    c += len(flashed)

print(c)

k = 0
# BFS
while True:
    k += 1
    g2 += 1
    q = deque()
    flashed = set()
    for i in range(m):
        for j in range(n):
            if g2[i, j] > 9 and not (i, j) in flashed:
                q.append((i, j))
                flashed.add((i, j))
    while q:
        i, j = q.popleft()
        for di, dj in d:
            i_, j_ = i + di, j + dj
            if 0 <= i_ < m and 0 <= j_ < n:
                g2[i_, j_] += 1
                if g2[i_, j_] > 9 and not (i_, j_) in flashed:
                    q.append((i_, j_))
                    flashed.add((i_, j_))
    g2[g2 > 9] = 0
    if (g2 == 0).all(): break

print(k)
