from math import log10, floor

def blk(x, n):
    if (x, n) in c: return c[(x, n)]
    if n == 0:
        c[(x, n)] = 1
    elif x == 0:
        c[(x, n)] = blk(1, n - 1)
    else:
        l = floor(log10(x)) + 1
        if l % 2:
            c[(x, n)] = blk(x * 2024, n - 1)
        else:
            l = 10 ** (l // 2)
            c[(x, n)] = blk(x // l, n - 1) + blk(x % l, n - 1)
    return c[(x, n)]

c = {}
f = open('input')
s = [int(x) for x in f.readline().split()]
print(sum(blk(x, 25) for x in s))
print(sum(blk(x, 75) for x in s))
