def bd(s):
    i = 0
    j = 0
    t = []
    dt = []
    d = {}
    for x in s:
        if not j:
            d[i] = [len(t), int(x)]
            t.extend([i] * int(x))
            j = 1 - j
            i += 1
        else:
            dt.append([len(t), int(x)])
            t.extend([None] * int(x))
            j = 1 - j
    return t, dt, d, i - 1

def mv(s):
    i, j = 0, len(s) - 1
    while True:
        while s[i] != None: i += 1
        while s[j] == None: j -= 1
        if i > j: break
        s[i] = s[j]
        s[j] = None
    return j + 1

def mvf(s, t, d, x):
    while True:
        ft = False
        for i in t:
            if i[0] > d[x][0]: break
            if i[1] >= d[x][1]:
                ft = True
                break
        if ft:
            for j in range(d[x][1]):
                s[i[0] + j] = x
                s[d[x][0] + j] = None
            i[0], i[1] = i[0] + j + 1, i[1] - j - 1
        x -= 1
        if not x: break
    
f = open('input')
s = f.readline()[:-1]
#s = '2333133121414131402'
s, t, d, x = bd(s)
s1 = s[:]
n = mv(s1)
mvf(s, t, d, x)
print(sum(i * x for i, x in zip(range(n), s1)))
print(sum(i * x for i, x in zip(range(len(s)), s) if x != None))
