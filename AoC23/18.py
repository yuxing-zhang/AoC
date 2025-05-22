from collections import defaultdict as dd

# part 1
f = open('input')
p = [0, 0]
s = {(0, 0)}
d = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
lb, ub, rb, db = float('inf'), float('inf'), -float('inf'), -float('inf')
for l in f:
    i, j, k = l.split()
    j = int(j)
    for _ in range(j):
        p[0] += d[i][0]
        p[1] += d[i][1]
        s.add((p[0], p[1]))
    lb = min(lb, p[1])
    ub = min(ub, p[0])
    rb = max(rb, p[1])
    db = max(db, p[0])
f.close()
s_ = {(x + 1 - ub, y + 1 - lb) for (x, y) in s}
'''
m = [['.'] * (rb - lb + 3) for _ in range(db - ub + 3)]
for x, y in s:
    m[x + 1 - ub][y + 1 - lb] = '#'
print('\n'.join(''.join(l) for l in m))
'''
g = [[[] for _ in range(rb - lb + 3)] for __ in range(db - ub + 3)]
for i in range(db - ub + 3):
    for j in range(rb - lb + 3):
        if (i, j) not in s_:
            for k in d.values():
                x, y = i + k[0], j + k[1]
                if 0 <= x < db - ub + 3 and 0 <= y < rb - lb + 3 and\
                        (x, y) not in s_:
                    g[i][j].append((x, y))

def visit(g, u, visited):
    global c
    c += 1
    visited[u[0]][u[1]] = True
    for v in g[u[0]][u[1]]:
        if not visited[v[0]][v[1]]:
            visit(g, v, visited)

c = 0
visited = [[False] * len(g[0]) for _ in range(len(g))]
st = [(0, 0)]
while st:
    u = st.pop()
    if not visited[u[0]][u[1]]:
        visited[u[0]][u[1]] = True
        c += 1
        for v in g[u[0]][u[1]]:
            st.append(v)
print((rb - lb + 3) * (db - ub + 3) - c)

# part 2
f = open('input')
m = dd(list)
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
p = [0, 0]
l = [_.split()[-1][2:-1] for _ in f]
l = [(int(_[-1]), int(_[:-1], base=16)) for _ in l]
for k, (i, j) in enumerate(l):
    print(i, j)
    if i == 0:
        m[p[0]].append((p[1], p[1] + j, True if l[k - 1][0] == l[k + 1][0]\
                else False))
    elif i == 2:
        m[p[0]].append((p[1] - j, p[1], True if l[k - 1][0] == l[k + 1][0]\
                else False))
    elif i == 1:
        for k in range(p[0] + 1, p[0] + j):
            m[k].append(p[1])
    else:
        for k in range(p[0] - 1, p[0] - j, -1):
            m[k].append(p[1])
    p[0] += d[i][0] * j
    p[1] += d[i][1] * j
f.close()

c = 0
for v in m.values():
    v_ = sorted(v, key=lambda x: x if type(x) == int else x[0])
    flag = False
    for i in v_:
        if not flag:
            if type(i) == int:
                flag = True
                c += 1
                p = i
            else:
                c += i[1] - i[0] + 1
                if i[2]:
                    flag = True
                    p = i[1]
        else:
            if type(i) == int:
                flag = False
                c += i - p
            elif i[2]:
                flag = False
                c += i[1] - p
print(c)
