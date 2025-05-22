f = open('input')
x1, y1 = 0, 0
x2, y2, aim = 0, 0, 0
for l in f:
    d, n = l.split()
    n = int(n)
    if d == 'forward':
        x1 += n
        x2 += n
        y2 += aim * n
    elif d == 'down':
        y1 += n
        aim += n
    elif d == 'up':
        y1 -= n
        aim -= n
print(x1 * y1, x2 * y2)
