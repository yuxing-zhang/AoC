f = open('input')
mp = [list(l[:-1]) for l in f]
f.close()

m, n = len(mp), len(mp[0])
k = 0
for i in range(m):
    for j in range(n):
        if mp[i][j] == 'S':
            mp[i][j] = '.'
            k = 1
            break
    if k == 1:
        break
s = (i, j)

def p(m):
    print('\n'.join(''.join(_) for _ in m))
def move(d, mp, m, n, s, steps):
    di = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque([s])

    for i in range(steps):
        while True:
            j, k = q.popleft()
            if d[j][k] > i:
                q.appendleft((j, k))
                break
            for v in di:
                j_, k_ = j + v[0], k + v[1]
                if 0 <= j_ < m and 0 <= k_ < n and mp[j_][k_] == '.' and\
                        d[j_][k_] <= i:
                    q.append((j_, k_))
                    d[j_][k_] = i + 1

# part 1
from collections import deque

d = [[0] * n for _ in range(m)]
move(d, mp, m, n, s, 64)
t = 0
for i in range(m):
    for j in range(n):
        if d[i][j] == 64:
            t += 1
print(t)

# part 2
mp5 = [l * 5 for l in mp] * 5
d5 = [[0] * 5 * n for _ in range(5 * m)]
s5 = (327, 327)
move(d5, mp5, 5 * m, 5 * n, s5, 327)
c = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        for i_ in range(131 * i, 131 * (i + 1)):
            for j_ in range(131 * j, 131 * (j + 1)):
                if d5[i_][j_] == 327:
                    c[i][j] += 1
a = (26501365 - 65) // 131

def f(a):
    t = 0
    t = c[0][2] + c[2][0] + c[2][4] + c[4][2] + c[1][0] + c[1][4] + c[3][0] +\
            c[3][4]
    t += (c[1][0] + c[1][1] + c[1][3] + c[1][4] + c[3][0] + c[3][1] +\
            c[3][3] + c[3][4]) * (a - 1)
    t += c[1][2] * a ** 2 + c[2][2] * (a - 1) ** 2
    return t
print(f(a))
