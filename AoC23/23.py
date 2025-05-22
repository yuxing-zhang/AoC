from collections import defaultdict as dd

f = open('input')
mp = [l[:-1] for l in f]
m, n = len(mp), len(mp[0])
f.close()

def visit(u, t, e, visited, c):
    global s
    if u == e and c > s:
        s = c
    visited.add(u)
    for v in t[u]:
        if v not in visited:
            visit(v, t, e, visited, c + 1)
    visited.remove(u)

# part 1
t = dd(list)
d = [(0, 1), (-1, 0), (0, -1), (1, 0)]
for i in range(m):
    for j in range(n):
        if mp[i][j] == '.':
            for v in d:
                i_, j_ = i + v[0], j + v[1]
                if 0 <= i_ < m and 0 <= j_ < n and mp[i_][j_] != '#':
                    t[(i, j)].append((i_, j_))
        elif mp[i][j] == '>':
            t[(i, j)].append((i, j + 1))
        elif mp[i][j] == '^':
            t[(i, j)].append((i - 1, j))
        elif mp[i][j] == '<':
            t[(i, j)].append((i, j - 1))
        elif mp[i][j] == 'v':
            t[(i, j)].append((i + 1, j))

s = 0
e = (m - 1, n - 2)
st = [(0, 1, 0)]
visited = set()
while st:
    x, y, c = st.pop()
    if (x, y) in visited:
        visited.remove((x, y))
        continue
    visited.add((x, y))
    st.append((x, y, c))
    if (x, y) == e and c > s:
        s = c
    for v in t[(x, y)]:
        if v not in visited:
            st.append((v[0], v[1], c + 1))

print(s)

# part 2
t = dd(list)
d = [(0, 1), (-1, 0), (0, -1), (1, 0)]
for i in range(m):
    for j in range(n):
        if mp[i][j] != '#':
            for v in d:
                i_, j_ = i + v[0], j + v[1]
                if 0 <= i_ < m and 0 <= j_ < n and mp[i_][j_] != '#':
                    t[(i, j)].append((i_, j_))

t_ = dd(list)
st = [((0, 1), (0, 1), 0)]
e = (m - 1, n - 2)
visited = set()
while st:
    u, p, c = st.pop()
    if u in visited:
        continue
    visited.add(u)
    for v in t[u]:
        if len(t[v]) != 2:
            if v != p:
                t_[p].append((v, c + 1))
                t_[v].append((p, c + 1))
                st.append((v, v, 0))
        else:
            st.append((v, p, c + 1))

s = 0
st = [t_[(0, 1)][0]]
visited = set()
while st:
    u, c = st.pop()
    if u in visited:
        visited.remove(u)
        continue
    visited.add(u)
    st.append((u, c))
    if u == t_[e][0][0]:
        if c > s:
            s = c
        continue
    for v, c_ in t_[(u)]:
        if v not in visited:
            st.append((v, c + c_))

print(s + t_[e][0][1])
'''
us = list(t_)
cache = dd(lambda : float('inf'))
for i in t_:
    for j, k in t_[i]:
        cache[(i, j, -1)] = k

def dist(s, t, i):
    if (s, t, i) in cache or i == -1:
        return cache[(s, t, i)]
    c = dist(s, t, i - 1)
    v = us[i]
#    if v not in (s, t):
    c = min(dist(s, v, i - 1) + dist(v, t, i - 1), c)
    cache[(s, t, i)] = c
    return c
print(dist((0, 1), (m - 1, n - 2), len(us) - 1)) 
'''
