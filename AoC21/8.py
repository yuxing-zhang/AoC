# part 1
a = []

with open('input.txt') as f:
    for l in f:
        l = l[:-1]
        l = l.split()[-4:]
        a.extend([x for x in l if len(x) in {2, 3, 4, 7}])

# part 2
import collections
# f maps a line in the input file to the corresponding  4 digit number
def f(s:str) -> int:
    s = s[:-1].split()
    x, y = s[:10], s[-4:]
    c = collections.Counter(''.join(x))
    d = {}
    # d maps a wire to the correct segment. d is built
    # by counting the number of occurrence of each letter
    # b e f have unique # of occurence, only need to
    # distinguish between (a, c) and (d, g)
    # This can be achieved by inspecting digit 4
    for i in x:
        if len(i) == 4: break
    for k in c:
        if c[k] == 6: d[k] = 'b'; continue
        if c[k] == 4: d[k] = 'e'; continue
        if c[k] == 9: d[k] = 'f'; continue
        if c[k] == 8:
            if k in i: d[k] = 'c'
            else: d[k] = 'a'
            continue
        if c[k] == 7:
            if k in i: d[k] = 'd'
            else: d[k] = 'g'
    z = [''.join(sorted(d[i] for i in j)) for j in y]
    # global variable g contains the standard digit representation
    return g[z[0]] * 1000 + g[z[1]] * 100 + g[z[2]] * 10 + g[z[3]]


g = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4,
     'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}

with open('input.txt') as ff:
    print(sum(f(l) for l in ff))

