def cb(x):
    d = [0, 1, 2, 3, a, b, c]
    return d[x]

def f0(x):
    global a
    a //= 2 ** cb(x)

def f1(x):
    global b
    b ^= x

def f2(x):
    global b
    b = cb(x) % 8

def f3(x):
    global a
    if a:
        global p
        p = x - 2

def f4(x):
    global b
    b ^= c

def f5(x):
    s.append(cb(x) % 8)

def f6(x):
    global b
    b = a // 2 ** cb(x)

def f7(x):
    global c
    c = a // 2 ** cb(x)
op = [f0, f1, f2, f3, f4, f5, f6, f7]

a, b, c = 236555997372013, 0, 0
p = 0
l = [2,4,1,3,7,5,4,7,0,3,1,5,5,5,3,0]

p = 0
s = []
while p < len(l):
    op[l[p]](l[p + 1])
    p += 2
print(','.join(str(x) for x in s))

def check(i, a):
    if i < 0:
        print(a)
        return
    for j in range(8):
        b = j ^ 3
        c = (a * 8 + j) // 2 ** b
        if (b ^ c ^ 5) % 8 == l[i]:
            check(i - 1, a * 8 + j)
check(len(l) - 1, 0)
'''
print(a, j, end=' ')
j = j ^ 3; print(j, end=' ')
c = a // 2 ** b; print(c, end=' ')
j = j ^ c; print(j, end=' ')
print(a // 8, end=' ')
print(j ^ 5)
print(a)
'''
