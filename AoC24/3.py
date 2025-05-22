import re

f = open('input')
#s = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

s = 0
on = True
for l in f:
    for t in re.findall('mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)', l):
        if t == 'do()':
            on = True
            continue
        if t == 'don\'t()':
            on = False
            continue
        if on:
            x, y = t[4:-1].split(',')
            s += int(x) * int(y)
print(s)
