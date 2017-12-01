#   Pandigital multiples

from functools import reduce


def check_pan_digital(n, digits):
    a = (reduce(lambda rst, d: rst * 10 + d, range(1, digits + 1)))
    n = ''.join(sorted(n))
    return int(n) == a


ans = 0
for i in range(10000, 9000, -1):
    num = str(i) + str(2 * i)
    if check_pan_digital(num, 9):
        ans = max(ans, int(num))
print(ans)
