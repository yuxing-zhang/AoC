def fx(s, x):
    t = set()
    for i, j in s:
        t.add((2 * x - i if i > x else i, j))
    return t

def fy(s, y):
    t = set()
    for i, j in s:
        t.add((i, 2 * y - j if j > y else j))
    return t

def draw(s):
    xmax, ymax = max(x for x, y in s), max(y for x, y in s)
    mat = [['.'] * (xmax + 1) for _ in range(ymax + 1)]
    for x, y in s:
        mat[y][x] = '#'
    print('\n'.join(''.join(r) for r in mat))

f = open('input')
s = set()
for l in f:
    if len(l) == 1: break
    s.add(tuple(int(x) for x in l[:-1].split(',')))

for l in f:
    xy, n = l.split()[-1].split('=')
    n = int(n)
    s = fx(s, n) if xy == 'x' else fy(s, n)
    print(len(s))

draw(s)
