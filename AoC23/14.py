from collections import Counter
f = open('input')
m = [list(l[:-1]) for l in f]
f.close()

def p(m):
    print('\n'.join(''.join(_) for _ in m))
    print()
# part 1
for i in range(1, len(m)):
    for j, x in enumerate(m[i]):
        if x == 'O':
            for k in range(i, 0, -1):
                if m[k - 1][j] == '.':
                    m[k - 1][j], m[k][j] = m[k][j], m[k - 1][j]
                else:
                    break
print(sum(x * y for (x, y) in zip((Counter(l)['O'] for l in m), range(len(m),
        0, -1))))

# part 2
f = open('input')
m = [list(l[:-1]) for l in f]
f.close()
def c():
    for i in range(1, len(m)):
        for j, x in enumerate(m[i]):
            if x == 'O':
                for k in range(i, 0, -1):
                    if m[k - 1][j] == '.':
                        m[k - 1][j], m[k][j] = m[k][j], m[k - 1][j]
                    else:
                        break
    for i in range(len(m)):
        for j, x in enumerate(m[i][1:], 1):
            if x == 'O':
                for k in range(j, 0, -1):
                    if m[i][k - 1] == '.':
                        m[i][k - 1], m[i][k] = m[i][k], m[i][k - 1]
                    else:
                        break
    for i in range(-2, -len(m) - 1, -1):
        for j, x in enumerate(m[i]):
            if x == 'O':
                for k in range(i, -1):
                    if m[k + 1][j] == '.':
                        m[k + 1][j], m[k][j] = m[k][j], m[k + 1][j]
                    else:
                        break
    for i in range(len(m)):
        for j in range(-2, -len(m[0]) - 1, -1):
            if m[i][j] == 'O':
                for k in range(j, -1):
                    if m[i][k + 1] == '.':
                        m[i][k + 1], m[i][k] = m[i][k], m[i][k + 1]
                    else:
                        break
d = {}
i = 0
while True:
    c()
    i += 1
    t = ''.join(''.join(_) for _ in m)
    if t in d:
        j = i
        i = d[t]
        break
    d[t] = i
for _ in range((1000000000 - i) % (j - i)):
    c()
print(sum(x * y for (x, y) in zip((Counter(l)['O'] for l in m), range(len(m),
        0, -1))))
