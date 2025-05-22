from functools import cmp_to_key
f = open('input')

c = set()
for l in f:
    if '|' in l:
        x, y = l[:-1].split('|')
        x, y = int(x), int(y)
        c.add((x, y))
    else:
        break

def check(s):
    d = dict(zip(s, range(len(s))))
    for x, y in c:
        if x in d and y in d and d[x] > d[y]: return False
    return True

S, T = 0, 0
for l in f:
    s = [int(x) for x in l[:-1].split(',')]
    if check(s):
        S += s[len(s) // 2]
    else:
        T += sorted(s, key=cmp_to_key(lambda x, y: -1 if (x, y) in c else\
                    (1 if (y, x) in c else 0)))[len(s) // 2]
print(S, T)
