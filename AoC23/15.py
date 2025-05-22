from collections import OrderedDict as OD

def h(s):
    return sum(ord(c) * 17 ** i for (c, i) in zip(s[::-1], range(1, len(s)+1)))\
            % 256

f = open('input')
l = f.readline()
f.close()

# part 1
d = {}
s = 0
for i in l[:-1].split(','):
    if i not in d:
        d[i] = h(i)
    s += d[i]
print(s)

# part 2
b = [OD() for _ in range(256)]
for i in l[:-1].split(','):
    if i[-1] == '-':
        j = i[:-1]
        k = h(j)
        if j in b[k]: del b[k][j]
    else:
        j = i[:-2]
        k = h(j)
        b[k][j] = int(i[-1])
s = 0
for i, x in enumerate(b, 1):
    for j, y in enumerate(x, 1):
        s += i * j * x[y]
print(s)
