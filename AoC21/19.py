from collections import Counter

def rot(x, y, z):
    return [(x, y, z), (x, z, -y), (x, -y, -z), (x, -z, y),\
            (y, z, x), (y, x, -z), (y, -z, -x), (y, -x, z),\
            (z, x, y), (z, y, -x), (z, -x, -y), (z, -y, x),\
            (-x, y, -z), (-x, -z, -y), (-x, -y, z), (-x, z, y),\
            (-y, x, z), (-y, z, -x), (-y, -x, -z), (-y, -z, x),\
            (-z, y, x), (-z, -x, y), (-z, -y, -x), (-z, x, -y)] 

def cal(s, t):
    for t_ in zip(*[rot(x, y, z) for x, y, z in t]):
        c = Counter()
        for x, y, z in s:
            for x_, y_, z_ in t_:
                c[(x - x_, y - y_, z - z_)] += 1
        d = c.most_common(1)[0]
        if d[1] >= 12:
            return [(x + d[0][0], y + d[0][1], z + d[0][2]) for\
                    x, y, z in t_], d[0]

f = open('input')
ss = []
for l in f:
    if len(l) == 1:
        ss.append(s)
    elif l[1] == '-':
        s = []
    else:
        s.append(tuple(int(x) for x in l[:-1].split(',')))
ss.append(s)

sss = set(ss[0])
i = set(range(1, len(ss)))
o = [(0, 0, 0)]
while i:
    for j in i:
        s = cal(sss, ss[j])
        if s:
            sss |= set(s[0])
            o.append(s[1])
            i.discard(j)
            break
#print(len(sss))
import numpy as np
x, y = np.array(o)[:, None, :], np.array(o)
print(np.abs((x - y)).sum(axis=-1).max())
