import numpy as np

# helper function to translate array representating a number to that number
def array2int(a):
    return int(''.join(str(s) for s in a), base=2)

# read data into a numpy 2d array
with open('input.txt') as f:
    a = [[int(c) for c in l[:-1]] for l in f]
    a = np.array(a)

# part 1
x = (a.sum(axis=0) > len(a) // 2).astype(int)
y = 1 - x

print(array2int(x) * array2int(y))

# part 2
aa, bb = a, a
for i in range(12):
    ta = aa.sum(axis=0)[i]
    if ta >= (len(aa) + 1) // 2:
        aa = aa[aa[:, i] == 1]
    else:
        aa = aa[aa[:, i] == 0]
    if len(aa) == 1: break

for i in range(12):
    tb = bb.sum(axis=0)[i]
    if tb >= (len(bb) + 1) // 2:
        bb = bb[bb[:, i] == 0]
    else:
        bb = bb[bb[:, i] == 1]
    if len(bb) == 1: break

print(array2int(aa[0]) * array2int(bb[0]))
