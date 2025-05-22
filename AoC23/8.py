f = open('input')
m = [0 if _ == 'L' else 1 for _ in f.readline()[:-1]]
n = len(m)
f.readline()
g = {}
a = []
for l in f:
    t = l.split()
    g[t[0]] = (t[2][1:-1], t[3][:-1])
    if t[0][-1] == 'A':
        a.append(t[0])

# part 1
i = 0
v = 'AAA'
while v != 'ZZZ':
    v = g[v][m[i % n]]
    i += 1
print(i)

# part 2
from functools import reduce
from math import gcd

s = []
for v in a:
    i = 0
    j = 0
    while True:
        v = g[v][m[i % n]]
        i += 1
        if v[-1] == 'Z':
            s.append(i)
            break
print(s)
print(reduce(lambda x, y: x * y // gcd(x, y), s))
