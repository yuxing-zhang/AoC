from collections import defaultdict as dd
from functools import reduce

d = dd(list)
f = open('input')
for l in f:
    if len(l) == 1:
        break
    i = l.index('{')
    k = l[:i]
    for s in l[i + 1:-2].split(','):
        j = s.find(':')
        d[k].append((s[0], s[1], int(s[2:j]), s[j+1:]) if j != -1 else s)

# part 1
def check(e):
    p = 'in'
    while True:
        for c in d[p]:
            if not type(c) == tuple:
                p = c
                break
            if c[1] == '<' and e[c[0]] < c[2] or c[1] == '>' and\
                    e[c[0]] > c[2]:
                p = c[3]
                break
        if p == 'A':
            return True
        if p == 'R':
            return False

s = 0
for l in f:
    e = {i[0]: int(i[2:]) for i in l[1:-2].split(',')}
    if check(e):
        s += sum(e.values())
print(s)
f.close()

# part 2
def visit(u, e):
    if u == 'R':
        return
    if u == 'A':
        a.append(e)
        return
    for v in d[u]:
        if type(v) == tuple:
            i, j = e[v[0]]
            e_ = e.copy()
            if v[1] == '<':
                e_[v[0]] = (i, min(j, v[2] - 1))
                e[v[0]] = (max(i, v[2]), j)
            else:
                e_[v[0]] = (max(i, v[2] + 1), j)
                e[v[0]] = (i, min(j, v[2]))
            if e_[v[0]][0] <= e_[v[0]][1]:
                visit(v[3], e_)
            if e[v[0]][0] > e[v[0]][1]:
                break
        else:
            visit(v, e)

a = []
e = {i: (1, 4000) for i in 'xmas'}
visit('in', e)
print(sum(reduce(lambda x, y: x * y, (j - i + 1 for (i, j) in b.values()))\
        for b in a))
