class N():
    def __init__(self, x, y, p=None, b=None):
        self.x, self.y, self.p, self.b = x, y, p, b

    def find(self, n):
        if not n: return self
        z = self.x.find(n - 1) if isinstance(self.x, N) else None
        return z if z else (self.y.find(n - 1) if isinstance(self.y, N)\
                            else None)
    def exp(self):
        u = self
        while u.p and u.b == 0:
            u = u.p
        if u.p:
            u = u.p
            if not isinstance(u.x, N):
                u.x += self.x
            else:
                u = u.x
                while isinstance(u.y, N):
                    u = u.y
                u.y += self.x
        u = self
        while u.p and u.b == 1:
            u = u.p
        if u.p:
            u = u.p
            if not isinstance(u.y, N):
                u.y += self.y
            else:
                u = u.y
                while isinstance(u.x, N):
                    u = u.x
                u.x += self.y
        if self.b: self.p.y = 0
        else: self.p.x = 0

    def spl(self):
        if isinstance(self.x, N) and self.x.spl(): return True
        if not isinstance(self.x, N) and self.x >= 10:
            self.x = N(self.x // 2, (self.x + 1) // 2, self, 0)
            return True
        if isinstance(self.y, N) and self.y.spl(): return True
        if not isinstance(self.y, N) and self.y >= 10:
            self.y = N(self.y // 2, (self.y + 1) // 2, self, 1)
            return True
        return False

    def mag(self):
        return 3 * (self.x.mag() if isinstance(self.x, N) else self.x) +\
               2 * (self.y.mag() if isinstance(self.y, N) else self.y)
 
    def __add__(self, n):
        t = N(self, n)
        self.p, self.b = t, 0
        n.p, n.b = t, 1
        while True:
            e = t.find(4)
            if e:
                e.exp()
                continue
            if t.spl():
                continue
            break
        return t

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
def build(s):
    stk = []
    i = 0
    while i < len(s):
        if '0' <= s[i] <= '9':
            x = 0
            while '0' <= s[i] <= '9':
                x = 10 * x + int(s[i])
                i += 1
            stk.append(x)
            continue
        if s[i] == ']':
            y, x = stk.pop(), stk.pop()
            z = N(x, y)
            stk.append(z)
            if isinstance(x, N):
                x.p, x.b = z, 0
            if isinstance(y, N):
                y.p, y.b = z, 1
        i += 1
    return z

f = open('input_')
from itertools import permutations, product
ns = [l[:-1] for l in f]
s = 0
for i, j in permutations(ns, 2):
    t = (build(i) + build(j)).mag()
    if t > s:
        s = t
print(s)

n = build(ns[0])
for l in ns[1:]:
    n = n + build(l)
print(n.mag())
