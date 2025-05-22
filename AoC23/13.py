def g(r, c=0):
    n = len(r) // 2
    for i in range(0, n):
        flag = True
        for j in range(i + 1, 2 * i + 2):
            if r[j] != r[2 * i + 1 - j]:
                flag = False
                break
        if flag and i + 1 != c:
            return i + 1
    for i in range(n, len(r) - 1):
        flag = True
        for j in range(2 * i - len(r) + 2, i + 1):
            if r[j] != r[2 * i + 1 - j]:
                flag = False
                break
        if flag and i + 1 != c:
            return i + 1
    return 0

# part 1 & 2
f = open('input')
m = []
s1 = s2 = 0
while True:
    l = f.readline()
    if len(l) > 1:
        m.append(l[:-1])
    else:
        r = [int(''.join(map(lambda x: '1' if x == '#' else '0', _)), base=2)
            for _ in m]
        c = [int(''.join(map(lambda x: '1' if x == '#' else '0', _)), base=2)
            for _ in zip(*m)]
        a, b = len(m), len(m[0])
        t1 = g(r)
        p = 0
        if not t1:
            t1 = g(c)
            p = 1
            s1 += t1
        else:
            s1 += t1 * 100
        for i in range(0, a):
            flag = False
            for j in range(0, b):
                if m[i][j] == '#':
                    r[i] -= 1 << (b - 1 - j)
                    c[j] -= 1 << (a - 1 - i)
                else:
                    r[i] += 1 << (b - 1 - j)
                    c[j] += 1 << (a - 1 - i)
                t2 = g(c, t1) if p else g(c)
                if not t2:
                    t2 = (g(r) if p else g(r, t1)) * 100
                    if not t2:
                        if m[i][j] == '#':
                            r[i] += 1 << (b - 1 - j)
                            c[j] += 1 << (a - 1 - i)
                        else:
                            r[i] -= 1 << (b - 1 - j)
                            c[j] -= 1 << (a - 1 - i)
                        continue
                s2 += t2
                flag = True
                break
            if flag: break
        m = []
        if not l: break
print(s1, s2)
f.close()
