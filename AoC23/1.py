def g(l):
# get the 2-digit number form a line
    for i in l:
        if '0' <= i <= '9':
            a = i
            break
    for i in l[::-1]:
        if '0' <= i <= '9':
            b = i
            break
    print(a + b)
    return int(a + b)
 
# part 1
f = open('input')
s = 0
for l in f:
   s += g(l)
print(s)
f.close()

# part 2
def h(l):
# replace words with digits
    f = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six':
    '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    b = {'eno': '1', 'owt': '2', 'eerht': '3', 'ruof': '4', 'evif': '5', 'xis':
    '6', 'neves': '7', 'thgie': '8', 'enin': '9'}
    flag = False
    print(l[:-1])
    for i in range(len(l)):
        for j in f:
            if l[i:i + len(j)] == j:
                l = l[:i] + f[j] + l[i:]
                flag = True
                break
        if flag: break
    flag = False
    for i in range(len(l) - 1, -1, -1):
        for j in b:
            if l[i:i - len(j):-1] == j:
                l = l[:i + 1] + b[j] + l[i + 1:]
                flag = True
                break
        if flag: break
    print(l[:-1])
    return l

s = 0
f = open('input')
for l in f:
    s += g(h(l))
print(s)
f.close()

