import numpy as np

# part 1 & 2
def p(a):
# s extrapolate at the right and t at the left
    s = 0
    t = 0
    i = 1
    while a.any():
        s += a[-1]
        t += a[0] * i
        i *= -1
        a = a[1:] - a[:-1]
    return s, t

f = open('input')
s, t = 0, 0
for l in f:
    r = p(np.array([int(x) for x in l.split()]))
    s += r[0]
    t += r[1]
print(s, t)
