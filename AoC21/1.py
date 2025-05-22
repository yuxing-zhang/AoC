import numpy as np
f = open('input')
dpth = np.array([int(l[:-1]) for l in f])

print((dpth[1:] > dpth[:-1]).sum())
print((dpth[3:] > dpth[:-3]).sum())
