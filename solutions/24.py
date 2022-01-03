#   Lexicographic permutations

import itertools
from functools import reduce

a = itertools.permutations(range(10))
index = 1000000
i = 1
for x in a:
    if i == index:
        print(reduce(lambda rst, d: rst * 10 + d, x))
        break
    i += 1
