from collections import defaultdict as DD
f = open('input')
M = 16777216
'''
s = 0
for l in f:
    x = int(l[:-1])
    for _ in range(2000):
        x = (x * 64 ^ x) % M
        x = (x // 32 ^ x) % M
        x = (x * 2048 ^ x) % M
    s += x
print(s)
'''
d = DD(dict)
for k, l in enumerate(f):
    x = int(l[:-1])
    s = [x % 10]
    for i in range(2000):
        x = (x * 64 ^ x) % M
        x = (x // 32 ^ x) % M
        x = (x * 2048 ^ x) % M
        s.append(x % 10) 
        if i >= 3:
            t = tuple(s[j] - s[j - 1] for j in range(-4, 0))
            if k not in d[t]:
                d[t][k] = s[-1]
print(max(sum(v_ for v_ in v.values()) for v in d.values()))
