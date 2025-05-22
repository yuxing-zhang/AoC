import numpy as np
f = open('input')

c = 0
for l in f:
    s = np.array([int(x) for x in l.split()])
    d = s[1:] - s[:-1]
    i, j = min(d), max(d)
    if d[0] > 0 and 1 <= i and j <= 3 or d[0] < 0 and -3 <= i and j <= -1:
        c += 1

print(c)
f.close()

from collections import Counter
c = 0
f = open('input')
for l in f:
    s = np.array([int(x) for x in l.split()])
    d = s[1:] - s[:-1]
    n = len(d)
    ct = Counter(d)
    p = 1
    if (d > 0).sum() > n / 2:
        t = n - ct[1] - ct[2] - ct[3]
    else:
        t = n - ct[-1] - ct[-2] - ct[-3]
        p = -1
    if t >= 3: continue
    if t == 0:
        c += 1
        continue
    i, j = -1, -1
    for k, x in enumerate(d):
        if x * p < 1 or x * p > 3:
            if i < 0: i = k
            else: j = k
    if j >= 0:
        if i + 1 == j and 1 <= p * (d[i] + d[j]) <= 3:
            c += 1
    else:
        if i == 0 or i == n - 1:
            c += 1
        elif 1 <= p * (d[i - 1] + d[i]) <= 3 or\
             1 <= p * (d[i] + d[i + 1]) <= 3:
            c += 1
print(c)

