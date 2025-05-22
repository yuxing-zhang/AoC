f = open('input')
m = 0
ob = set()
for i, l in enumerate(f):
    for j, c in enumerate(l):
        if c == '#': ob.add((i, j))
        elif c == '^': a, b = i, j
m, n = i + 1, j

t = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
x, y = a, b
dx, dy = -1, 0
r = {(x, y)}
while True:
    x_, y_ = x + dx, y + dy
    if x_ < 0 or x_ >= m or y_ < 0 or y_ >= n:
        break
    if (x_, y_) not in ob:
        r.add((x_, y_))
        x, y = x_, y_
    else:
        dx, dy = t[(dx, dy)]
print(len(r))

def check(i, j):
    x, y = a, b
    dx, dy = -1, 0
    r = {(x, y, dx, dy)}
    ob_ = ob | {(i, j)}
    while True:
        x_, y_ = x + dx, y + dy
        if x_ < 0 or x_ >= m or y_ < 0 or y_ >= n:
            return False
        if (x_, y_) not in ob_:
            if (x_, y_, dx, dy) in r:
                return True
            r.add((x_, y_, dx, dy))
            x, y = x_, y_
        else:
            dx, dy = t[(dx, dy)]

print(sum(check(i, j) for i in range(m) for j in range(n)))
