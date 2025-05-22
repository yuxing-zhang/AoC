import numpy as np

f = open('input')
s = [int(x) for x in f.readline()[:-1].split(',')]
f.readline()
mats, mat = [], []
for l in f:
    if len(l) == 1:
        mats.append(mat)
        mat = []
        continue
    mat.append([int(x) for x in l.split()])
mats.append(mat)
mats = np.array(mats)
zs = np.zeros_like(mats)

def check():
    for x in s:
        zs[mats == x] = 1
        for m, z in zip(mats, zs):
            for r in z:
                if (r == 1).all():
                    return m, z, x
            for c in z.T:
                if (c == 1).all():
                    return m, z, x
m, z, x = check()
print(x * m[z == 0].sum())

zs = np.zeros_like(mats)
won = [0] * len(zs)
for x in s:
    zs[mats == x] = 1
    for i in range(len(zs)):
        if not won[i]:
            for r in zs[i]:
                if (r == 1).all():
                    m_, z_, x_ = mats[i], zs[i].copy(), x
                    won[i] = 1
            for c in zs[i].T:
                if (c == 1).all():
                    m_, z_, x_ = mats[i], zs[i].copy(), x
                    won[i] = 1
print(x_ * m_[z_ == 0].sum())
