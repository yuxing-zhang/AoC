from collections import defaultdict as dd
f = open('input')
bs = []
for k, l in enumerate(f):
    i = l.index('~')
    s, t = l[:i].split(','), l[i + 1:-1].split(',')
    bs.append((k, [int(j) for j in s], [int(j) for j in t]))
f.close()

n = len(bs)
d = {}
d_to, d_from = dd(set), dd(set)
bs.sort(key=lambda x: x[1][2])
for b in bs:
    if b[1][2] == 1:
        for i in range(b[1][0], b[2][0] + 1):
            for j in range(b[1][1], b[2][1] + 1):
                for h in range(b[1][2], b[2][2] + 1):
                    d[(i, j, h)] = b[0]
        continue
    flag = 0
    for k in range(b[1][2], 0, -1):
        for i in range(b[1][0], b[2][0] + 1):
            for j in range(b[1][1], b[2][1] + 1):
                if (i, j, k - 1) in d:
                    flag = 1
                    break
            if flag: break
        if flag: break
    for i in range(b[1][0], b[2][0] + 1):
        for j in range(b[1][1], b[2][1] + 1):
            for h in range(b[2][2] + 1 - b[1][2]):
                d[(i, j, k + h)] = b[0]
            if (i, j, k - 1) in d:
                d_to[d[(i, j, k - 1)]].add(b[0])
                d_from[b[0]].add(d[(i, j, k - 1)])

# part 1
s = 0
for k, v in d_to.items():
    flag = 1
    for v_ in v:
        if len(d_from[v_]) == 1:
            flag = 0
            break
    if flag:
        s += 1
print(s + len([k for k in d_from if k not in d_to]) +
        len([k for k in range(n) if k not in d_from and k not in d_to]))

# part 2
def rm(d_from, i):
    if i in cache:
        return cache[i]
    if len(d_to) == 1:
        j = list(d_to[i])[0]
        if len(d_from[j]) == 1:
            cache[i] = 1 + rm(d_from, j)
        return cache[i]
    def _visit(j):
        nonlocal c
        c += 1
        if j not in d_to:
            return
        for k in d_to[j]:
            d_from[k].remove(j)
            if not d_from[k]:
                _visit(k)
    c = 0
    _visit(i)
    cache[i] = c - 1
    return c

cache = {}
for i in d_to:
    rm({k: v.copy() for (k, v) in d_from.items()}, i)
print(sum(cache.values()))
