f = open('input')

def run(w, z, i):
    if i == 14:
        raise Exception
    W[i] = w
    a, b, c = p[i]
    if a == 1:
        z = z * 26 + w + c
        for w in range(1, 10):
#        for w in range(9, 0, -1):
            run(w, z, i + 1)
    else:
        x = z % 26 + b
        if w == x:
            for w in range(1, 10):
#            for w in range(9, 0, -1):
                run(w, z // 26, i + 1)

p = []
for i, l in enumerate(f):
    j = i % 18
    if j == 0:
        p.append([])
    elif j in (4, 5, 15):
        p[-1].append(int(l.split()[-1]))

W = [None] * 14
try:
    for w in range(1, 10):
#    for w in range(9, 0, -1):
        run(w, 0, 0)
except Exception:
    print(''.join(str(w) for w in W))
