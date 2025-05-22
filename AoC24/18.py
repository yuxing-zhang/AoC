from collections import defaultdict as DD, deque

class H():
    def __init__(self, g):
        self.t = [[u, float('inf')] for u in g]
        self.i = {u[0]: i for i, u in enumerate(self.t)}

    def pop(self):
        del  self.i[self.t[0][0]]
        if len(self.t) == 1:
            return self.t.pop()
        x = self.t[0]
        self.t[0] = self.t.pop()
        self.i[self.t[0][0]] = 0
        i, j = 0, 1
        while j < len(self.t):
            if j + 1 < len(self.t) and self.t[j + 1][1] < self.t[j][1]:
                j += 1
            if self.t[j][1] >= self.t[i][1]:
                break
            self.t[i], self.t[j] = self.t[j], self.t[i]
            self.i[self.t[i][0]], self.i[self.t[j][0]] = i, j
            i, j = j, 2 * j + 1
        return x
    
    def update(self, u, n):
        '''
        if p[u][0] == n:
            p[u][1].add(v)
        elif p[u][0] > n:
            p[u] = [n, {v}]
        '''
        if u not in self.i:
            return
        i = self.i[u]
        if self.t[i][1] <= n: return
        self.t[i][1] = n
        while i > 0:
            j = (i - 1) // 2
            if self.t[j][1] <= self.t[i][1]:
                break
            self.t[i], self.t[j] = self.t[j], self.t[i]
            self.i[self.t[i][0]], self.i[self.t[j][0]] = i, j
            i = j

f = open('input')
p = [tuple(int(x) for x in l[:-1].split(',')) for l in f]
m, n = 71, 71
dest = m - 1, n - 1
d = [(0, 1), (-1, 0), (0, -1), (1, 0)]
'''
for i in range(m):
    for j in range(n):
        for di, dj in d:
            i_, j_ = i + di, j + dj
            if 0 <= i_ < m and 0 <= j_ < n and (i_, j_) not in s:
                g[(i, j)].add((i_, j_))
'''
def check(a):
    s = p[:a]
    q = deque([(0, 0)])
    l = {(0, 0): 0}
    while q:
        u = q.popleft()
        for di, dj in d:
            v = u[0] + di, u[1] + dj
            if 0 <= v[0] < m and 0 <= v[1] < n and v not in s and v not in l:
                q.append(v)
                l[v] = l[u] + 1
    return l[dest] if dest in l else None

print(check(1024))
i, j = 0, len(p) - 1
while j - i > 1:
    k = (i + j) // 2
    if check(k): i = k
    else: j = k
print(p[i])
