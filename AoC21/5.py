import numpy as np

mat = np.zeros((1000, 1000))

f = open('input')
for l in f:
    l = l.split()
    xy0, xy1 = l[0], l[-1]
    x0, y0 = xy0.split(',')
    x1, y1 = xy1.split(',')
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    '''
    if x0 == x1:
        y0, y1 = (y0, y1) if y0 <= y1 else (y1, y0)
        mat[y0:y1 + 1, x0] += 1
    elif y0 == y1:
        x0, x1 = (x0, x1) if x0 <= x1 else (x1, x0)
        mat[y0, x0:x1 + 1] += 1
    '''
    mat[range(y0, y1 + 1) if y0 < y1 else range(y0, y1 - 1, -1),
        range(x0, x1 + 1) if x0 < x1 else range(x0, x1 - 1, -1)] += 1

print((mat > 1).sum())
