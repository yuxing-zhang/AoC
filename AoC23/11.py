f = open('input')
m = []
g = []
r, c = [], []
for i, l in enumerate(f):
    m.append(l[:-1])
    k = False
    for j, x in enumerate(l):
        if x == '#':
            g.append((i, j))
            k = True
    if not k:
        r.append(i)
f.close()
for j in range(len(m[0])):
    k = False
    for i in range(len(m)):
        if m[i][j] == '#': k = True
    if not k:
        c.append(j)

# part 1
s = 0
for i, x in enumerate(g[:-1]):
    for y in g[i+1:]:
        ri, rj = (x[0], y[0]) if x[0] < y[0] else (y[0], x[0])
        ci, cj = (x[1], y[1]) if x[1] < y[1] else (y[1], x[1])
        t = rj - ri + cj - ci
        for j in r:
            if ri < j < rj: t += 1
        for j in c:
            if ci < j < cj: t += 1
        s += t
print(s)

# part 2
s = 0
for i, x in enumerate(g[:-1]):
    for y in g[i+1:]:
        ri, rj = (x[0], y[0]) if x[0] < y[0] else (y[0], x[0])
        ci, cj = (x[1], y[1]) if x[1] < y[1] else (y[1], x[1])
        t = rj - ri + cj - ci
        for j in r:
            if ri < j < rj: t += 999999
        for j in c:
            if ci < j < cj: t += 999999
        s += t
print(s)
