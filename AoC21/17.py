from math import ceil, floor, sqrt

def f():
    c = 0
    flg = False
    tx0 = ceil((-1 + sqrt(1 + 8 * x0)) / 2)
    tx1 = floor((-1 + sqrt(1 + 8 * x1)) / 2)
    for vy in range(y1, 0, -1):
        t0 = ceil((1 - 2 * vy + sqrt((2 * vy - 1) ** 2 + 8 * y0)) / 2)
        t1 = floor((1 - 2 * vy + sqrt((2 * vy - 1) ** 2 + 8 * y1)) / 2)
        if t0 > t1: continue
        vxu = set(range(tx0, min(tx1 + 1, 2 * vy + t1)))
        for t in range(2 * vy - 1 + t0, 2 * vy + t1):
            vx0 = ceil(x0 / t + (t - 1) / 2)
            vx1 = floor(x1 / t + (t - 1) / 2)
            vxu |= set(range(max(vx0, t), vx1 + 1))
        c += len(vxu)
        if not flg and vxu:
            flg = True
            hmax = (vy - 1) * vy // 2

        vxd = set(range(tx0, min(tx1, t1) + 1))
        for t in range(t0, t1 + 1):
            vx0 = ceil(x0 / t + (t - 1) / 2)
            vx1 = floor(x1 / t + (t - 1) / 2)
            vxd |= set(range(max(vx0, t), vx1 + 1))
        c += len(vxd)
    print(hmax, c)

def sim(vx, vy):
    x, y = 0, 0
    while y >= -y1:
        x += vx
        y += vy
#        print(x, y)
        vy -= 1
        vx -= 1 if vx else 0
        if x0 <= x <= x1 and -y1 <= y <= -y0: return True
    return False

x0, x1, y0, y1 = 155, 215, 72, 132
#x0, x1, y0, y1 = 20, 30, 5, 10
f()
