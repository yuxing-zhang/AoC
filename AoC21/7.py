# a contains the data

import numpy as np

a = np.array(sorted(a))

mid = a[len(a) // 2]

# part 1
print(np.abs(a - mid).sum())

# part 2
print(min(((a - a[i])**2 + abs(a - a[i])).sum() for i in range(1000)) // 2)
