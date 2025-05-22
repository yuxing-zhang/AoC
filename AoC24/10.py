from collections import defaultdict

def vstr(u):
    if u in c: return
    if h[u[0]][u[1]] == 9:
        c[u] = 1
        hd[u] = {u}
        return
    for v in g[u]:
        vstr(v)
        c[u] += c[v]
        hd[u] |= hd[v]

def vst(u):
    s = [u]
    while s:
        u = s.pop()
        if u in c:
            if c[u] == 0:
                for v in g[u]:
                    c[u] += c[v]
                    hd[u] |= hd[v]
            continue
        if h[u[0]][u[1]] == 9:
            c[u] = 1
            hd[u] = {u}
            continue
        s.append(u)
        c[u] = 0
        for v in g[u]:
            s.append(v)

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bd(mat, m, n):
    g = defaultdict(set)
    for i in range(m):
        for j in range(n):
            for di, dj in d:
                i_, j_ = i + di, j + dj
                if 0 <= i_ < m and 0 <= j_ < n and mat[i_][j_]-mat[i][j] == 1:
                    g[(i, j)].add((i_, j_))
    return g

f = open('input')
h = [[int(x) for x in l[:-1]] for l in f]
m, n = len(h), len(h[0])
g = bd(h, m, n)
#print(g); exit()
sh, sp = 0, 0
c = defaultdict(int)
hd = defaultdict(set)
for i in range(m):
    for j in range(n):
        if h[i][j] == 0:
            vst((i, j))
            sh += len(hd[(i, j)])
            sp += c[(i, j)]
print(sh, sp)
