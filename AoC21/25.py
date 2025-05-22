import numpy as np

# We save the input data into a np ndarray, where 1 and -1 correspond
# to moving east and south respectively, and 0 correspond. to empty
# space.
d = {'>': 1, 'v': -1, '.': 0}
with open('input.txt') as f:
    a = np.array([[d[x] for x in l[:-1]] for l in f])

class Map():
    def __init__(self, m):
        self.m = m
    def move(self):
        # s, t represent east moving elements and elements whose right
        # hand side neighbor is empty. Therefore, the eligible elements
        # can be obtained by s * t
        s = self.m == 1
        t = np.concatenate([self.m[:, 1:], self.m[:, :1]], axis=1) == 0
        # Move from
        mf = s * t

        # flag to check if any element can move in this step
        f = mf.any()

        # Move to
        mt = np.concatenate([mf[:, -1:], mf[:, :-1]], axis=1)
        self.m[mt] = 1
        self.m[mf] = 0

        # The above algorithm applies to elements moving south
        s = self.m == -1
        t = np.concatenate([self.m[1:], self.m[:1]]) == 0
        mf = s * t

        f = f or mf.any()

        mt = np.concatenate([mf[-1:], mf[:-1]])
        self.m[mt] = -1
        self.m[mf] = 0

        return f

map = Map(a)
i = 0
while (map.move()): i += 1
print(i+1)
