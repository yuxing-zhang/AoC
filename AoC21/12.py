from collections import defaultdict as DD
c = 0
def vst1(u, pth):
    if u == 'end':
        global c
        c += 1
        return
    vstd.add(u)
    for v in g[u]:
        if v[0] > 'Z' and v in vstd:
            continue
        vst1(v)
    vstd.discard(u)

def vst2(u):
    if u == 'end':
        global c
        c += 1
#        print(pth + '-end')
        return
    global twice
    if u[0] > 'Z' and u in vstd: twice = u
    vstd.add(u)
    for v in g[u]:
        if v[0] > 'Z' and v in vstd and twice or v == 'start':
            continue
        vst2(v)
    if u == twice: twice = None
    else: vstd.discard(u)


f = open('input')
g = DD(list)
for l in f:
    u, v = l[:-1].split('-')
    g[u].append(v)
    g[v].append(u)

vstd = set()
#vst1('start')
#print(c)

vstd = set()
twice = None
c = 0
vst2('start')
print(c)
