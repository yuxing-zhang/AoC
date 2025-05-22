f = open('input')
s = [l[:-1] for l in f]
m, n = len(s), len(s[0])

c = 0
d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

for i in range(m):
    for j in range(n):
        if s[i][j] == 'X':
            for i_, j_ in d:
                if 0 <= i + i_ * 3 < m and 0 <= j + j_ * 3 < n and\
                   s[i + i_][j + j_] == 'M' and\
                   s[i + i_ * 2][j + j_ * 2] == 'A' and\
                   s[i + i_ * 3][j + j_ * 3] == 'S':
                    c += 1
print(c)

c = 0
for i in range(1, m - 1):
    for j in range(1, n - 1):
        if s[i][j] == 'A' and\
           (s[i - 1][j - 1] == 'M' and s[i + 1][j + 1] == 'S' or\
           s[i - 1][j - 1] == 'S' and s[i + 1][j + 1] == 'M') and\
           (s[i - 1][j + 1] == 'M' and s[i + 1][j - 1] == 'S' or\
           s[i - 1][j + 1] == 'S' and s[i + 1][j - 1] == 'M'):
            c += 1
print(c)

