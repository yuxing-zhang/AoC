def parse(l):
    i = l.find(':')
    j = l.find('|')
    n = int(l[4:i])
    s = set(int(x) for x in l[i+1:j].split())
    t = set(int(x) for x in l[j+1:].split())
    return n, s, t

# part 1
f = open('input')
s = 0
# matches
m = []
for l in f:
    _, r, t = parse(l)
    n = len(r & t)
    m.append(n)
    if n: s += 2 ** (n - 1)
print(s)
f.close()

# part 2
c = [1] * len(m)
for i, j in enumerate(c):
    for k in range(m[i]):
        c[i + k + 1] += j
print(sum(c))
