from collections import defaultdict as DD

f = open('input')
mat = [l[:-1] for l in f]
m, n = len(mat), len(mat[0])
g = []
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for i, r in enumerate(mat):
    gr = []
    for j, x in enumerate(r):
        gr.append(set())
        for d in ds:
            i_, j_ = i + d[0], j + d[1]
            if 0 <= i_ < m and 0 <= j_ < n and mat[i_][j_] == mat[i][j]:
                gr[j].add((i_, j_))
    g.append(gr)

def vst(i, j):
    if vstd[i][j]:
        return
    vstd[i][j] = True
    global nc, ec, sd
    sd |= {(i - .5, j), (i, j + .5), (i + .5, j), (i, j - .5)}
    nc += 1
    ec += len(g[i][j])
    for i_, j_ in g[i][j]:
        sd -= {((i + i_) / 2, (j + j_) / 2)}
        vst(i_, j_)

def h(s):
    g = DD(list)
    for i, j in s:
        if isinstance(i, int):
            if (i + 1, j) in s and (i + .5, j + .5) not in s:
                g[(i, j)].append((i + 1, j))
            if (i - 1, j) in s and (i - .5, j + .5) not in s:
                g[(i, j)].append((i - 1, j))
        else:
            if (i, j + 1) in s and (i + .5, j + .5) not in s:
                g[(i, j)].append((i, j + 1))
            if (i, j - 1) in s and (i + .5, j - .5) not in s:
                g[(i, j)].append((i, j - 1))
    c = 0
    stk = []
    vstd = set()
    for i, j in s:
        if not (i, j) in vstd:
            stk.append((i, j))
            c += 1
            while stk:
                u = stk.pop()
                if u in vstd: continue
                vstd.add(u)
                for v in g[u]: stk.append(v)
    return c

vstd = [[False] * n for _ in range(m)]
rg = []
for i in range(m):
    for j in range(n):
        if not vstd[i][j]:
            nc, ec, sd = 0, 0, set()
            vst(i, j)
            rg.append((nc, 4 * nc - ec, h(sd)))

print(sum(a * p for a, p, _ in rg), sum(a * s for a, _, s in rg))
