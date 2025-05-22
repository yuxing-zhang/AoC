import numpy as np

def ply(x, y, a, b):
    if (x, y, a, b) in c:
        return c[(x, y, a, b)]
    if x < 0 or y < 0:
        return float('inf')
    if x == y == 0:
        return 0
    t = float('inf')
    if a:
        t = min(3 + ply(x - ax, y - ay, a - 1, b), t)
    if b:
        pb = ply(x - bx, y - by, a, b - 1)
        t = min(1 + ply(x - bx, y - by, a, b - 1), t)
    c[(x, y, a, b)] = t
    return t

f = open('input')
s, t = 0, 0
e = 1e-3
while True:
    l = f.readline().split()
    if not len(l):
        break
    ax, ay = int(l[-2][2:-1]), int(l[-1][2:])
    l = f.readline().split()
    bx, by = int(l[-2][2:-1]), int(l[-1][2:])
    l = f.readline().split()
    x, y = int(l[-2][2:-1]), int(l[-1][2:])
    l = f.readline()
    a, b = np.linalg.inv([[ax, bx], [ay, by]]) @ np.array([x, y])
    if abs(a - round(a)) < e and abs(b - round(b)) < e:
        s += 3 * a + b
    a, b = np.linalg.inv([[ax, bx], [ay, by]]) @ np.array([x +
            10000000000000, y + 10000000000000])
    if abs(a - round(a)) < e and abs(b - round(b)) < e:
        t += 3 * a + b
print(s, t)

