from itertools import combinations
from collections import defaultdict as DD

V, E, T, nb = set(), set(), set(), DD(set)
f = open('input')
for l in f:
    u, v = l[:-1].split('-')
    V.add(u); V.add(v)
    E.add((u, v)); E.add((v, u))
    nb[u].add(v)
    nb[v].add(u)
    if u[0] == 't': T.add(u)
    if v[0] == 't': T.add(v)
print(sum(1 for u, v, w in combinations(V, 3)\
        if (u, v) in E and (v, w) in E and (w, u) in E and {u, v, w} & T))

clq = [set()]
for i, v in enumerate(V):
    if i % 100 == 0:
        print(i)
    c = [s | {v} for s in clq if not s - nb[v]]
    clq.extend(c)
l = 0
for s in clq:
    if len(s) > l:
        l = len(s)
        smax = s
print(','.join(sorted(smax)))
