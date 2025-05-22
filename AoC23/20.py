from collections import deque, defaultdict as dd
from functools import reduce

tp = dd(lambda : -1)
t = dd(list)
q = deque()
f = open('input')
for l in f:
    l_ = l.split()
    if l_[0] == 'broadcaster':
        for i in l_[2:-1]:
            t['b'].append(i[:-1])
            q.append((None, i[:-1], 0))
        t['b'].append(l_[-1])
        q.append((None, l_[-1], 0))
    else:
        u = l_[0][1:]
        for i in l_[2:-1]:
            t[u].append(i[:-1])
        t[u].append(l_[-1])
        if l_[0][0] == '%':
            tp[u] = 0
        else:
            tp[u] = 1
f.close()

s = {}
def init():
    for i in tp:
        if tp[i] == 0:
            s[i] = 0
        else:
            s[i] = {}
    for i in t:
        for j in t[i]:
            if tp[j] == 1:
                s[j][i] = 0
    s['rx'] = 0

def run(q):
    c, con = [1, 0], set()
    while q:
        w, u, p = q.popleft()
        if w in {'mj', 'qs', 'rd', 'cs'} and p == 0:
            con.add(w)
        c[p] += 1
        if tp[u] == 0:
            if p == 0:
                s[u] = 1 - s[u]
                for v in t[u]:
                    q.append((u, v, s[u]))
        elif tp[u] == 1:
            s[u][w] = p
            p = 0
            for i in s[u].values():
                if i == 0:
                    p = 1
                    break
            for v in t[u]:
                q.append((u, v, p))
        elif u == 'rx' and p == 0:
            s[u] += 1
    return c, con

# part 1
c = []
k = 0
init()
while True:
    if k == 1000:
        break
    k += 1
    c.append(run(q.copy())[0])
    flag = 0
    for i in s:
        if tp[i] == 0:
            if s[i]:
                flag = 1
        elif tp[i] == 1:
            for j in s[i]:
                if s[i][j]:
                    flag = 1
                    break
        if flag == 1:
            break
    if flag == 0:
        break
m, n = 1000 // len(c), 1000 % len(c)
a, b = reduce(lambda x, y: [x[0] + y[0], x[1] + y[1]], c)
a_, b_ = reduce(lambda x, y: [x[0] + y[0], x[1] + y[1]], c[:n], [0, 0])
print((a * m + a_) * (b * m + b_))

# part 2
tp['rx'] = 2
init()
'''
import networkx as nx
from matplotlib import pyplot as plt
g = nx.DiGraph()
for i, j in t.items():
    for k in j:
        g.add_edge(i, k)
nx.draw_networkx(g)
plt.show()
'''
a = 1
j = 0
while True:
    j += 1
    _, k = run(q.copy())
    if k:
        print(j, k)
# print the lcm
