from functools import reduce

def bd():
    global p, versum
    ver, tid = int(s[p:p + 3], 2), int(s[p + 3:p + 6], 2)
    versum += ver
    p += 6
    if tid == 4:
        t = 0
        while True:
            t = 16 * t + int(s[p + 1:p + 5], 2)
            p += 5
            if s[p - 5] == '0': break
        return t
    pkts = []
    if s[p] == '0':
        l = int(s[p + 1:p + 16], 2)
        p += 16
        p_ = p + l
        while p != p_:
            pkts.append(bd())
    else:
        n = int(s[p + 1:p + 12], 2)
        p += 12
        for _ in range(n):
            pkts.append(bd())
    return reduce(op[tid], pkts)

op = {0: lambda x, y: x + y,
      1: lambda x, y: x * y,
      2: lambda x, y: min(x, y),
      3: lambda x, y: max(x, y),
      5: lambda x, y: x > y,
      6: lambda x, y: x < y,
      7: lambda x, y: x == y
     }
f = open('input')
s = bin(int(f.readline()[:-1], 16))[2:]
s = (4 - len(s) % 4) % 4 * '0' + s
p = 0
versum = 0
print(bd() )
print(versum)
