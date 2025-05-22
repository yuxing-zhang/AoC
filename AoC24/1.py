import numpy as np

f = open('input')
s = np.array([[int(x) for x in l.split()] for l in f])
s.sort(axis=0)
print(np.abs(s[:, 0] - s[:, 1]).sum())
f.close()

from collections import Counter
d = Counter(s[:, 1])
print(sum(x * d[x] for x in s[:, 0]))
