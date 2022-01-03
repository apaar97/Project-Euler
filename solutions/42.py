#   Coded triangle numbers

import math


def check_square(n):
    return int(math.sqrt(n)) ** 2 == n


with open('inputs/42.txt', 'r') as f:
    a = (f.read().strip().split(','))
f.close()
ans = 0
for i in range(len(a)):
    x = sum((ord(c) - 64) for c in a[i][1:-1])
    if check_square(8 * x + 1):
        ans += 1
print(ans)
