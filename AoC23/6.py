from math import ceil, sqrt

def g(t, d):
    return 2 * ceil(sqrt((t/2)**2 - d) - 1) + 1 if t % 2 == 0\
      else 2 * ceil(.5 + sqrt(t**2 - 4 * d) / 2 - 1)

# part 1
f = open('input')
t = [int(x) for x in f.readline().split()[1:]]
d = [int(x) for x in f.readline().split()[1:]]
p = 1
for i, j in zip(t, d):
    print(g(i, j))
    p *= g(i, j)
print(p)
f.close()

# part 2
f = open('input')
t = int(''.join(f.readline().split()[1:]))
d = int(''.join(f.readline().split()[1:]))
print(g(t, d))
f.close()
