from functools import reduce

f = open('input')
c = {}
p = {}
q = {}
for l in f:
    if len(l) == 1: break
    k, v = l.split()
    k = k[:-1]
    p[k] = {k}
    q[k] = k
    c[k] = int(v)

t, m = {}, {}
V, Z = [], []
for l in f:
    u, o, v, _, w = l.split()
    t[w] = sorted([u, o, v])
    m[tuple(sorted([u, o, v]))] = w
    V.append(w)
    if w[0] == 'z':
        Z.append(w)

op = {'AND': lambda x, y: x & y,
      'OR': lambda x, y: x | y,
      'XOR': lambda x, y: x ^ y}

def vst(v):
    if v in c: return c[v]
    o, u, w = t[v]
    c[v] = op[o](vst(u), vst(w))
    p[v] = p[u] | p[w] | {v}
    q[v] = '(' + q[u] + ' ' + o + ' ' + q[w] + ')'
    return c[v]

for v in V:
    vst(v)

#for v in sorted(V):
#    if v[0] == 'z': print(v); print(q[v])
print(int(''.join(str(v) for k, v in sorted(c.items(), reverse=True)
        if k[0] == 'z'), base=2))
#print([v for k, v in sorted(c.items(), reverse=True) if k[0] == 'z'])
#print(set(V) - s - t)

# Cause error and manually check
carry = m[('AND', 'x00', 'y00')]
for n in range(1, 45):
    n = str(n) if n > 9 else '0' + str(n)
    x, y, z = 'x' + n, 'y' + n, 'z' + n
    o, u, v = t[z]
    xxory, xandy = m[('XOR', x, y)], m[('AND', x, y)]
    xorandc = m[('AND',) + tuple(sorted([xxory, carry]))]
    carry = m[('OR',) + tuple(sorted([xandy, xorandc]))]

