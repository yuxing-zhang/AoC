def check(s):
    stk = []
    for c in s:
        if c in lt:
            stk.append(c)
        elif stk[-1] != rt[c]:
            return c
        else:
            stk.pop()
    return stk

lt = set('([{<')
rt = {')': '(', ']': '[', '}': '{', '>': '<'}
lpt = {')': 3, ']': 57, '}': 1197, '>': 25137}
rpt = {'(': 1, '[': 2, '{': 3, '<': 4}

f = open('input')
s, sc = 0, []
while True:
    try:
        l = next(f)
        t = check(l[:-1])
        if isinstance(t, str):
            s += lpt[t]
            continue
        c = 0
        while t:
            c = c * 5 + rpt[t.pop()]
        sc.append(c)
    except StopIteration:
        break

sc.sort()
print(s, sc[len(sc) // 2])
