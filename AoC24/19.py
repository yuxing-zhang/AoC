from functools import reduce

def check(s):
    if s in c: return c[s]
    c[s] = sum((s[:len(t)] == t) * check(s[len(t):]) for t in ts)
    return c[s]

f = open('input')
ts = next(f).split()
for i, t in enumerate(ts[:-1]):
    ts[i] = t[:-1]
next(f)
c = {'': 1}
n = 0
while True:
    try:
        n += check(next(f)[:-1])
    except StopIteration:
        break
print(n)
