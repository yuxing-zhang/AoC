import numpy as np

def mv(d):
    i, j = x[0] + d[0], x[1] + d[1]
    while mat[i][j] == 'O':
        i, j = i + d[0], j + d[1]
    if mat[i][j] == '#':
        return
    mat[i][j], mat[x[0]][x[1]], mat[x[0] + d[0]][x[1] + d[1]] = 'O.@'
    x[0], x[1] = x[0] + d[0], x[1] + d[1]

def find(i, j, di):
    i_ = i + di
    if mat2[i_][j] == '#':
        return {(i, j)}, False
    if mat2[i_][j] == '.':
        return {(i, j)}, True
    if mat2[i_][j] == '[':
        fl, fr = find(i_, j, di), find(i_, j + 1, di)
        return fl[0] | fr[0] | {(i, j)}, fl[1] and fr[1]
    if mat2[i_][j] == ']':
        fl, fr = find(i_, j - 1, di), find(i_, j, di)
        return fl[0] | fr[0] | {(i, j)}, fl[1] and fr[1]

def mv2(d):
#    print(d, x2)
    if d[0] == 0:
        i, j = x2[0], x2[1] + d[1]
        while mat2[i][j] in '[]':
            j += d[1]
        if mat2[i][j] == '#':
            return
        mat2[i, x2[1] + d[1]:j + d[1]:d[1]] = mat2[i, x2[1]:j:d[1]]
        mat2[x2[0], x2[1]] = '.'
        x2[1] += d[1]
    else:
        s, mvbl = find(*x2, d[0])
        if mvbl:
            i, j = np.array(list(zip(*s)))
            t = mat2[i, j]
            mat2[i, j] = '.'
            mat2[i + d[0], j] = t
            x2[0] += d[0]


ds = {'<': (0, -1), '^': (-1, 0), '>': (0, 1), 'v': (1, 0)}
f = open('input')
mat = []
for i, l in enumerate(f):
    if len(l) == 1: break
    j = l.find('@')
    if j > -1:
        x = [i, j]
        x2 = [i, 2 * j]
    mat.append(list(l[:-1]))

tf = {'#': ['#', '#'], '.': ['.', '.'], 'O': ['[', ']'], '@': ['@', '.']}
mat2 = np.array([sum((tf[c] for c in r), []) for r in mat])
for l in f:
    for i in l[:-1]:
#        print(i)
        mv(ds[i])
        mv2(ds[i])
#print('\n'.join(''.join(r) for r in mat2))
s, s2 = 0, 0
for i, r in enumerate(mat):
    for j, c in enumerate(r):
        if c == 'O': s += 100 * i + j
for i, r in enumerate(mat2):
    for j, c in enumerate(r):
        if c == '[': s2 += 100 * i + j
print(s, s2)
