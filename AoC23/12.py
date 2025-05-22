def g(s, c):
    k = (s, c)
    if k in cache:
        return cache[k]
    if not c:
        cache[k] = 0 if '#' in s else 1
        return cache[k]
    if not s:
        cache[k] = 0
        return cache[k]
    m, n = len(s), c[0]
    i = 0
    while i < m and s[i] == '.': i += 1
    if i == m:
        cache[k] = 0
        return cache[k]
    if s[i] == '#':
        j = i
        while j < m and s[j] != '.': j += 1
        if j - i < n or j - i > n and s[i + n] == '#':
            cache[k] = 0
            return cache[k]
        cache[k] = g(s[i + n + 1:], c[1:])
        return cache[k]
    j = i
    while j < m and s[j] == '?': j += 1
    if j == m or s[j] == '.':
        if j - i < n:
            cache[k] = g(s[j + 1:], c)
            return cache[k]
        cache[k] = g(s[i + n + 1:], c[1:]) + g(s[i + 1:], c)
        return cache[k]
    if j - i <= n:
        a = j
        while a < m and s[a] == '#': a += 1
        b = a
        while b < m and s[b] != '.': b += 1
        if b - i < n:
            cache[k] = 0
            return cache[k]
        t = 0
        for it in range(i, j + 1):
            if a <= it + n <= b and (it + n == m or s[it + n] != '#'):
                t += g(s[it + n + 1:], c[1:])
        cache[k] = t
        return cache[k]
    cache[k] = g(s[i + n + 1:], c[1:]) + g(s[i + 1:], c)
    return cache[k]
cache = {}

# part 1
f = open('input')
t = 0
for l in f:
    s, c = l.split()
    c = tuple(int(x) for x in c.split(','))
    t += g(s, c)
print(t)
f.close()

# part 2
f = open('input')
t = 0
for l in f:
    s, c = l.split()
    c = tuple(int(x) for x in c.split(','))
    t += g('?'.join(s for _ in range(5)), c * 5)
print(t)
f.close()
