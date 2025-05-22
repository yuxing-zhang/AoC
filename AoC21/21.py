from collections import Counter
from itertools import cycle

# Part 1
# Initial positions and scores
p = [3, 5]
s = [0, 0]

die = cycle(range(1, 101))

# i determines which player rolls the die
i = 0
while s[0] < 1000 and s[1] < 1000:
    t = next(die) + next(die) + next(die)
    j = i % 2
    p[j] = (p[j] + t) % 10
    s[j] += p[j] if p[j] else 10
    i += 1

print(s[0] * i * 3 if s[0] < 1000 else s[1] * i * 3)

# Part 2
# Use dynamic programming.
# The idea is for each starting position, we build a 3-dimensional table
# U(n, p, s) = the # of universes in which the player at the nth step
# will be at positio p with a score of s. Then we can build upon U another
# table V(n, s) = # of universes in which the player at the nth step will
# have a score of s. Finally, the # of universes where player 1 wins
# equals \sum_{i=1} \sum_{s >= 21 > t} V_1[i, s] * V_2[i-1, t]

# At each round, 3 rolls will split each universe into 27 sub-universes.
# The table tb below maps the number of movements to the number of
# sub-universes in which that number of movements were taken.
tb = {3: 1,
      4: 3,
      5: 6,
      6: 7,
      7: 6,
      8: 3,
      9: 1
}
     
def f(p):
    # t[n][p][s] = U[n, p, s]
    t = [[Counter() for _ in range(10)]]
    t[0][p][0] = 1
    while True:
        n = [Counter() for _ in range(10)]
        for i in range(10):
            for s, c in t[-1][i].items():
                # Stop moving once score reaches 21
                if s < 21:
                    for m in tb:
                        j = (i + m) % 10
                        n[j][s + j if j else s + j + 10] += c * tb[m]
        # Stop looping if no more universe can be generated
        if sum(sum(i.values()) for i in n) == 0: break
        t.append(n)
    return t

# Build tables V from U
U = [f(3), f(5)]
V = [[sum(p, Counter()) for p in u] for u in U]
 
# w contains the # of universes in which each player wins
w = [0, 0]
for j in range(2):
    for i in range(1, len(V[j])):
        for s, c in V[j][i].items():
            if s >= 21:
                for p, q in V[1-j][i-1].items():
                    if p < 21: w[j] += c * q

print(max(w))















