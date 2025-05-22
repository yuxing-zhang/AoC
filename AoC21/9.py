import numpy as np
from collections import defaultdict

with open('input.txt') as f:
    data = np.array([[int(x) for x in l[:-1]] for l in f])

# part 1
# Matrices t, b, l, r corresponds to the upper, lower, left, right
# element of every element in the data matrix
# 10 makes sure the boundary element is always greater

t, b, l, r = np.ones((4, *data.shape)) * 10
t[1:] = data[:-1]
b[:-1] = data[1:]
l[:, 1:] = data[:, :-1]
r[:, :-1] = data[:, 1:]

# A low point can be identified by checking if it is smaller than
# every corresponding element in t, b, l, r
t, b, l, r = t-data>0, b-data>0, l-data>0, r-data>0
low = data[t*b*l*r]
print(low.sum() + len(low))

# part 2
# We add an edge between every pair of element (u, v) where u < 9 and
# v < 9, and run dfs to find the size of every connected component.
g = defaultdict(list)
for i in range(100):
    for j in range(100):
        if data[i, j] != 9:
            if i-1 >= 0 and data[i-1, j] != 9: g[(i, j)].append((i-1, j))
            if i+1 < 100 and data[i+1, j] != 9: g[(i, j)].append((i+1, j))
            if j-1 >= 0 and data[i, j-1] != 9: g[(i, j)].append((i, j-1))
            if j+1 < 100 and data[i, j+1] != 9: g[(i, j)].append((i, j+1))

visited = np.zeros(data.shape)
sizes = []

def visit(u):
    visited[u] = 1
    global s
    s += 1
    for v in g[u]:
        if not visited[v]: visit(v)

for u in g:
    if not visited[u]:
        s = 0
        visit(u)
        sizes.append(s)

print(np.array(sorted(sizes)[-3:]).prod())
