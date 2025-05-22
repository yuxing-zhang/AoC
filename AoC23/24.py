from itertools import combinations, permutations
from collections import defaultdict as dd
import numpy as np

f = open('input')
h = []
for l in f:
    i = l.index('@')
    s, t = l[:i].split(), l[i + 1:].split()
    for j in range(2):
        s[j] = s[j][:-1]
        t[j] = t[j][:-1]
    h.append(([int(k) for k in s], [int(k) for k in t]))
f.close()

# part 1
def check(i, j, m, n):
    a1, b1, c1, d1 = i
    a2, b2, c2, d2 = j
    if c1 * d2 == c2 * d1:
        return True if (a1 - a2) * d1 == (b1 - b2) * c1 else False
    x = (c1 * c2 * b1 - c1 * c2 * b2 + a2 * d2 * c1 - a1 * d1 * c2)/\
            (c1 * d2 - c2 * d1)
    y = (a1 * d1 * d2 - a2 * d1 * d2 + c2 * b2 * d1 - c1 * b1 * d2)/\
            (c2 * d1 - c1 * d2)
    return True if m <= x <= n and m <= y <= n and (x - a1) * c1 > 0 and\
            (x - a2) * c2 > 0 else False
'''
k = 0
m, n = 200000000000000, 400000000000000
for i, j in combinations(h, 2):
    if check((*i[0][:2], *i[1][:2]), (*j[0][:2], *j[1][:2]), m, n):
        k += 1
print(k)
'''

# part 2
(p11, p12, p13), (v11, v12, v13) = h[0]
(p21, p22, p23), (v21, v22, v23) = h[1]
(p31, p32, p33), (v31, v32, v33) = h[2]

A = np.empty((6, 6))
Y = np.empty((6, 1))
A[0, 0] = v12 - v22; A[0, 1] = v21 - v11; A[0, 3] = p22 - p12
A[0, 4] = p11 - p21
A[1, 0] = v22 - v32; A[1, 1] = v31 - v21; A[1, 3] = p32 - p22
A[1, 4] = p21 - p31
A[2, 1] = v13 - v23; A[2, 2] = v22 - v12; A[2, 4] = p23 - p13
A[2, 5] = p12 - p22
A[3, 1] = v23 - v33; A[3, 2] = v32 - v22; A[3, 4] = p33 - p23
A[3, 5] = p22 - p32
A[4, 2] = v11 - v21; A[4, 0] = v23 - v13; A[4, 5] = p21 - p11
A[4, 3] = p13 - p23
A[5, 2] = v21 - v31; A[5, 0] = v33 - v23; A[5, 5] = p31 - p21
A[5, 3] = p23 - p33

Y[0, 0] = p22 * v21 + p11 * v12 - p21 * v22 - p12 * v11
Y[1, 0] = p32 * v31 + p21 * v22 - p31 * v32 - p22 * v21
Y[2, 0] = p23 * v22 + p12 * v13 - p22 * v23 - p13 * v12
Y[3, 0] = p33 * v32 + p22 * v23 - p32 * v33 - p23 * v22
Y[4, 0] = p21 * v23 + p13 * v11 - p23 * v21 - p11 * v13
Y[5, 0] = p31 * v33 + p23 * v21 - p33 * v31 - p21 * v23

#print(np.linalg.inv(A) @ Y)
# The precision is not enough for P but we can find P using V
v1, v2, v3 = 201, 202, 79
a11, a12, a21, a22 = v1 - v11, v21 - v1, v2 - v12, v22 - v2
y1, y2 = p11 - p21, p12 - p22
t1 = (a22 * y1 - a12 * y2) / (a11 * a22 - a21 * a12)
print(p11 + (v11 - v1) * t1 + p12 + (v12 - v2) * t1 + p13 + (v13 - v3) * t1)
