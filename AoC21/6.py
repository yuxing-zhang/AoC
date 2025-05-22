f = open('input')
s = [0] * 9
for i in [int(x) for x in f.readline()[:-1].split(',')]:
    s[i] += 1

for i in range(256):
    t = s[0]
    for j in range(8):
        s[j] = s[j + 1]
    s[8] = t
    s[6] += t
    if i == 79:
        print(sum(s))

print(sum(s))
