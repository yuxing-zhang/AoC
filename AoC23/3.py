# part 1 and 2 in one go
# s stores the sum of part numbers
# d maps each * to its adjacent numbers
from collections import defaultdict
a = [None]

f = open('input')
# create the data matrix padded with . on 4 sides
for l in f:
    a.append('.' + l[:-1] + '.')
a.append('.' * len(a[1]))
a[0] = a[-1]
f.close()

S = '0123456789.'
s = 0
d = defaultdict(set)
for i, l in enumerate(a[1:-1], 1):
    j = 1
    while True:
        while a[i][j] < '0' or a[i][j] > '9':
            j += 1
            if j == len(a[0]):
                break
        if j == len(a[0]):
            break
        flag = False
        k = j
        # g contains adjacent * locations
        g = set()
        if a[i][j-1] not in S or a[i-1][j-1] not in S or a[i+1][j-1] not in S:
            flag = True
            if a[i][j-1] == '*': g.add((i, j-1))
            if a[i-1][j-1] == '*': g.add((i-1, j-1))
            if a[i+1][j-1] == '*': g.add((i+1, j-1))
        while '0' <= a[i][j] <= '9':
            if a[i-1][j] not in S or a[i+1][j] not in S:
                flag = True
                if a[i-1][j] == '*': g.add((i-1, j))
                if a[i+1][j] == '*': g.add((i+1, j))
            j += 1
        if a[i][j] not in S or a[i-1][j] not in S or a[i+1][j] not in S:
            flag = True
            if a[i][j] == '*': g.add((i, j))
            if a[i-1][j] == '*': g.add((i-1, j))
            if a[i+1][j] == '*': g.add((i+1, j))
        if flag:
            t = int(l[k:j])
            s += t
            for loc in g:
                d[loc].add(t)
print(s)
s = 0
for i, j in d.items():
    if len(j) == 2:
        t = list(j)
        s += t[0] * t[1]
print(s)
