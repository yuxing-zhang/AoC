def g(s):
    i0, i1, j0, j1 = float('inf'), -float('inf'), float('inf'), -float('inf')
    for i, j in s:
        if i < i0: i0 = i
        if i > i1: i1 = i
        if j < j0: j0 = j
        if j > j1: j1 = j
    t1 = {(i0 - 3, j0 - 3), (i0 - 3, j1 + 3), (i1 + 3, j0 - 3),\
          (i1 + 3, j1 + 3)}
    for i in range(i0 - 2, i1 + 3):
        t1 |= {(i, j0 - 3), (i, j0 - 2), (i, j1 + 2), (i, j1 + 3)}
    for j in range(j0 - 2, j1 + 3):
        t1 |= {(i0 - 3, j), (i0 - 2, j), (i1 + 2, j), (i1 + 3, j)}
    for i in range(i0 - 1, i1 + 2):
        for j in range(j0 - 1, j1 + 2):
            b = 256
            c = 0
            for i_ in range(-1, 2):
                for j_ in range(-1, 2):
                    if (i + i_, j + j_) in s:
                        c += b
                    b >>= 1
            if a[c] == '#':
                t1.add((i, j))

    t2 = set()
    for i in range(i0 - 2, i1 + 3):
        for j in range(j0 - 2, j1 + 3):
            b = 256
            c = 0
            for i_ in range(-1, 2):
                for j_ in range(-1, 2):
                    if (i + i_, j + j_) in t1:
                        c += b
                    b >>= 1
            if a[c] == '#':
                t2.add((i, j))
    return t2

def draw(s):
    i0, i1, j0, j1 = float('inf'), -float('inf'), float('inf'), -float('inf')
    for i, j in s:
        if i < i0: i0 = i
        if i > i1: i1 = i
        if j < j0: j0 = j
        if j > j1: j1 = j
    m = [['.'] * (j1 - j0 + 1) for _ in range(i1 - i0 + 1)]
    for i, j in s:
        m[i - i0][j - j0] = '#'
    print('\n'.join(''.join(i) for i in m))

f = open('input')
a = f.readline()[:-1]
f.readline()
s = {(i, j) for i, l in enumerate(f) for j, x in enumerate(l) if x == '#'}
for i in range(25):
    s = g(s)
print(len(s))
