from collections import defaultdict as DD

f = open('input')
p = DD(list)
for l in f:
    for i, c in enumerate(l):
        if c in 'ABCD':
            p[c].append(i - 1)
d = (2,) * 4 + (4,) * 4 + (6,) * 4 + (8,) * 4
e = [1] * 4 + [10] * 4 + [100] * 4 + [1000] * 4
s = set(d)

def check(p, mvd):
    if p == d:
        return 0
    if (p, mvd) in c: return c[(p, mvd)]
    t = float('inf')
    q = [False] * 11
    for x in p:
        if x not in s: q[x] = True
    for i, x in enumerate(p):
#        if i == 3 and mvd[6] or i == 0 and mvd[4] or\
#           i == 1 and mvd[7] or i == 5 and mvd[2]:
#            continue
        if i == 14 and mvd[12] or i == 9 and mvd[8] or\
           i == 5 and mvd[13] or i == 0 and mvd[4] or\
           i == 15 and mvd[14] or i == 6 and mvd[9] or\
           i == 1 and mvd[5] or i == 10 and mvd[0] or\
           i == 7 and mvd[15] or i == 2 and mvd[6] or\
           i == 3 and mvd[1] or i == 11 and mvd[10]:
            continue
        if x == d[i] and not mvd[i]: continue
        flg = True
        for j, y in enumerate(p):
            if y == d[i] != d[j]:
                flg = False
                break
        dlt = 1 if x < d[i] else -1
        for j in range(x + dlt, d[i], dlt):
            if q[j]:
                flg = False
        if flg:
            dt = e[i] * (d[i] - x) * dlt
            p_, m_ = mv(p, mvd, i, d[i])
            t_ = check(p_, m_)
            if t_ + dt < t:
                t = t_ + dt
                n[(p, mvd)] = (p_, m_)
#            t = min(t, check(*mv(p, mvd, i, d[i])) + dt)
            continue

        if mvd[i]:
            for j in range(x + 1, 11):
                if j not in s:
                    if q[j]: break
                    dt = e[i] * (j - x)
#                    t = min(t, check(*mv(p, mvd, i, j)) + dt)
                    p_, m_ = mv(p, mvd, i, j)
                    t_ = check(p_, m_)
                    if t_ + dt < t:
                        t = t_ + dt
                        n[(p, mvd)] = (p_, m_)
            for j in range(x - 1, -1, -1):
                if j not in s:
                    if q[j]: break
                    dt = e[i] * (x - j)
#                    t = min(t, check(*mv(p, mvd, i, j)) + dt)
                    p_, m_ = mv(p, mvd, i, j)
                    t_ = check(p_, m_)
                    if t_ + dt < t:
                        t = t_ + dt
                        n[(p, mvd)] = (p_, m_)
    c[(p, mvd)] = t
    return t

def mv(p, m, i, x):
    p_, m_ = list(p), list(m)
    p_[i], m_[i] = x, False
    p_, m_ = tuple(p_), tuple(m_)
    return p_, m_

c = {}
n = {}
p = tuple(i for c in 'ABCD' for i in p[c])
mvd = (True,) * 16
#print(check(p, mvd) + 5667)
print(check(p, mvd) + 19223)
t = p
m = mvd
while t != d:
    print(t)
    t, m = n[(t, m)]
