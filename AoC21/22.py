# Part 1 & part 2
def f(s, i, x):
    t = []
    while s:
        y = s.pop()
        if x[0] <= y[1] and x[1] >= y[0] and x[2] <= y[3] and x[3] >= y[2]\
                and x[4] <= y[5] and x[5] >= y[4]:
            if x[0] > y[0]:
                t.append((y[0], x[0] - 1, *y[2:]))
            if x[1] < y[1]:
                t.append((x[1] + 1, y[1], *y[2:]))
            x0, x1 = max(x[0], y[0]), min(x[1], y[1])
            if x[2] > y[2]:
                t.append((x0, x1, y[2], x[2] - 1, *y[4:]))
            if x[3] < y[3]:
                t.append((x0, x1, x[3] + 1, y[3], *y[4:]))
            y0, y1 = max(x[2], y[2]), min(x[3], y[3])
            if x[4] > y[4]:
                t.append((x0, x1, y0, y1, y[4], x[4] - 1))
            if x[5] < y[5]:
                t.append((x0, x1, y0, y1, x[5] + 1, y[5]))
        else:
            t.append(y)
    if i == 1:
        t.append(x)
    return t

s = [(0, 0, 0, 0, 0, 0)]
fi = open('input')
p1 = False
for l in fi:
    i, j = l.split()
    j = j.split(',')
    x = []
    for k in j:
        x.extend(k.split('..'))
    for k in [0, 2, 4]:
        x[k] = x[k][2:]
    if abs(int(x[0])) > 100 and not p1:
        print(sum(map(lambda x: (x[1] - x[0] + 1) * (x[3] - x[2] + 1) *\
                (x[5] - x[4] + 1), s)))
        p1 = True
    s = f(s, 1 if i == 'on' else 0, tuple(int(_) for _ in x))
fi.close()
print(sum(map(lambda x: (x[1] - x[0] + 1) * (x[3] - x[2] + 1) *\
        (x[5] - x[4] + 1), s)))
