from collections import defaultdict as dd

f = open('input')
m = [l[:-1] for l in f]
a, b = len(m), len(m[0])
f.close()

def g(i, j, v):
    if v in d[(i, j)]: return
    while 0 <= i < a and 0 <= j < b and m[i][j] == '.':
        d[(i, j)].add(v)
        i, j = i + v[0], j + v[1]
    if i < 0 or i >= a or j < 0 or j >= b: return
    d[(i, j)].add(v)
    if v == (0, 1):
        if m[i][j] == '-':
            g(i, j + 1, v)
        elif m[i][j] == '|':
            g(i - 1, j, (-1, 0))
            g(i + 1, j, (1, 0))
        elif m[i][j] == '\\':
            g(i + 1, j, (1, 0))
        elif m[i][j] == '/':
            g(i - 1, j, (-1, 0))
    elif v == (0, -1):
        if m[i][j] == '-':
            g(i, j - 1, v)
        elif m[i][j] == '|':
            g(i - 1, j, (-1, 0))
            g(i + 1, j, (1, 0))
        elif m[i][j] == '\\':
            g(i - 1, j, (-1, 0))
        elif m[i][j] == '/':
            g(i + 1, j, (1, 0))
    elif v == (1, 0):
        if m[i][j] == '-':
            g(i, j - 1, (0, -1))
            g(i, j + 1, (0, 1))
        elif m[i][j] == '|':
            g(i + 1, j, v)
        elif m[i][j] == '\\':
            g(i, j + 1, (0, 1))
        elif m[i][j] == '/':
            g(i, j - 1, (0, -1))
    elif v == (-1, 0):
        if m[i][j] == '-':
            g(i, j - 1, (0, -1))
            g(i, j + 1, (0, 1))
        elif m[i][j] == '|':
            g(i - 1, j, v)
        elif m[i][j] == '\\':
            g(i, j - 1, (0, -1))
        elif m[i][j] == '/':
            g(i, j + 1, (0, 1))
            
# part 1
d =  dd(set)
g(0, 0, (0, 1))
print(len(d) - len([k for k in d if not d[k]]))

# part 2
s = 0
for i in range(a):
    d = dd(set)
    g(i, 0, (0, 1))
    t = len(d) - len([k for k in d if not d[k]])
    if t > s: s = t
for i in range(b):
    d = dd(set)
    g(a - 1, i, (-1, 0))
    t = len(d) - len([k for k in d if not d[k]])
    if t > s: s = t
for i in range(a):
    d = dd(set)
    g(i, b - 1, (0, -1))
    t = len(d) - len([k for k in d if not d[k]])
    if t > s: s = t
for i in range(b):
    d = dd(set)
    g(0, i, (1, 0))
    t = len(d) - len([k for k in d if not d[k]])
    if t > s: s = t
print(s)
