from math import floor, log10

def check(p, c, cat=False):
    if p in c:
        return c[p]
    if cat:
        l = 10 ** (floor(log10(p[-1])) + 1)
    if len(p) == 3:
        c[p] = p[0] == p[1] + p[2] or p[0] == p[1] * p[2]
        if cat and not c[p] and p[0] == p[1] * l + p[2]:
            c[p] = True
    else:
        p_ = p[1:-1]
        c[p] = check((p[0] - p[-1],) + p_, c, cat) or\
               p[0] % p[-1] == 0 and check((p[0] // p[-1],) + p_, c, cat)
        if cat and not c[p] and\
           p[0] % l == p[-1] and check((p[0] // l,) + p_, c, cat):
            c[p] = True
    return c[p]

f = open('input')
s1, s2 = 0, 0
c1, c2 = {}, {}
for l in f:
    l = l.split()
    l[0] = int(l[0][:-1])
    for i in range(1, len(l)):
        l[i] = int(l[i])
    s1 += l[0] if check(tuple(l), c1) else 0
    s2 += l[0] if check(tuple(l), c2, True) else 0

print(s1, s2)
