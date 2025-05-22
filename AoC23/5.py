from functools import reduce

# closure on parameters
def h(p):
    def g(x):
        for i, j, k in p:
            if j <= x < j + k: return i + x - j
        return x
    return g

def parse(f):
    l = f.readline()
    seeds = [int(x) for x in l.split()[1:]]
    f.readline()
    maps = []
    params = []
    while True:
        f.readline()
        m = []
        while True:
            l = f.readline()
            if l == '\n' or l == '': break
            m.append([int(x) for x in l.split()])
        maps.append(h(m))    
        params.append(m)
        if l == '': break
    return seeds, maps, params

# part 1
f = open('input')
seeds, maps, params = parse(f)
f.close()

l = float('inf')
for s in seeds:
    for m in maps:
        s = m(s)
    if s < l:
        l = s
print(l)

# part 2
def comp(g, f):
# compose f and g to fg
    gx, gd, fy, fd = {}, {}, {}, {}
    s = []
    for y, x, d in g:
        gx[y] = x
        gd[y] = d
        s.append((y, 1, 'g'))
        s.append((y + d, 0, 'g'))
    for y, x, d in f:
        fy[x] = y
        fd[x] = d
        s.append((x, 1, 'f'))
        s.append((x + d, 0, 'f'))
    s.sort()
    m = []
    ff, fg = False, False
    for p, q, r in s:
        if q == 1:
            if r == 'g':
                fg = True
                ag = p
                if ff: m.append((fy[af] + a - af, a, p - a))
            if r == 'f':
                ff = True
                af = p
                if fg: m.append((a, gx[ag] + a - ag, p - a))
            a = p
        if q == 0:
            if r == 'g':
                fg = False
                if ff: m.append((fy[af] + a - af, gx[ag] + a - ag, p - a))
                else: m.append((a, gx[ag] + a - ag, p - a))
            if r == 'f':
                ff = False
                if fg: m.append((fy[af] + a - af, gx[ag] + a - ag, p - a))
                else: m.append((fy[af] + a - af, a, p - a))
            a = p
    return m

p = reduce(comp, params)
f = h(p)
m = float('inf')
for s, l in zip(seeds[::2], seeds[1::2]):
    t = f(s)
    for y, x, d in p:
        if s <= x < s + l and d > 0 and y < t: t = y
    if t < m: m = t

print(m)
