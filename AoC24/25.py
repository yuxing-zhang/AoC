import numpy as np

lock, key = [], []
f = open('input')
mat = []
for l in f:
    if len(l) == 1:
        mat = np.array(mat)
        if (mat[0] == '#').all():
            lock.append((mat[1:] == '#').sum(axis=0))
        else:
            key.append((mat[:-1] == '#').sum(axis=0))
        mat = []
        continue
    mat.append(list(l[:-1]))
c = 0
for k in key:
    for l in lock:
        if ((k + l) <= 5).all():
            c += 1
print(c)
