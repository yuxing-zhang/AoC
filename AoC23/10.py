f = open('input')
m = [list(l[:-1]) for l in f]
f.close()
d = {}
for i, r in enumerate(m):
     for j, x in enumerate(r):
        if x == 'S':
            m[i][j] = x = '7'
            s = (i, j)
        if x == '|': d[(i, j)] = [(i-1, j), (i+1, j)]
        elif x == '-': d[(i, j)] = [(i, j-1), (i, j+1)] 
        elif x == 'L': d[(i, j)] = [(i-1, j), (i, j+1)] 
        elif x == 'J': d[(i, j)] = [(i-1, j), (i, j-1)] 
        elif x == '7': d[(i, j)] = [(i+1, j), (i, j-1)] 
        elif x == 'F': d[(i, j)] = [(i+1, j), (i, j+1)] 

# part 1
visited = [[False] * (j + 1) for _ in range(i + 1)]
st = [s]
n = 0
c = set()
while st:
    v = st.pop()
    if not visited[v[0]][v[1]]:
        visited[v[0]][v[1]] = True
        n += 1
        c.add(v)
        if v[0] == 0 and m[v[0]][v[1]] == '-': s = v
        for u in d[v]:
            if not visited[u[0]][u[1]]:
                st.append(u)
print(n // 2)

# part 2
# unit normal vector
v = (1, 0)
e = set()
visited = [[False] * (j + 1) for _ in range(i + 1)]
while True:
    visited[s[0]][s[1]] = True
    t = s
    while True:
        t = (t[0] + v[0], t[1] + v[1])
        if t not in c:
            e.add(t)
        else: break
    if m[s[0]][s[1]] in '7L':
        if v == (0, -1): v = (1, 0)
        elif v == (0, 1): v = (-1, 0)
        elif v == (-1, 0): v = (0, 1)
        else: v = (0, -1)
        t = s
        while True:
            t = (t[0] + v[0], t[1] + v[1])
            if t not in c:
                e.add(t)
            else: break
    elif m[s[0]][s[1]] in 'FJ':
        if v == (0, -1): v = (-1, 0)
        elif v == (0, 1): v = (1, 0)
        elif v == (-1, 0): v = (0, -1)
        else: v = (0, 1)
        t = s
        while True:
            t = (t[0] + v[0], t[1] + v[1])
            if t not in c:
                e.add(t)
            else: break
    a, b = d[s]
    if not visited[a[0]][a[1]]:
        s = a
    else:
        s = b
        if visited[b[0]][b[1]]:
            break
print(len(e))
