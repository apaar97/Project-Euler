#   Pan digital products

from functools import reduce


def check_pan_digital(n, digits):
    a = (reduce(lambda rst, d: rst * 10 + d, range(1, digits + 1)))
    n = ''.join(sorted(n))
    return int(n) == a


ans = []
for a in range(1, 10000):
    for b in range(1, 10000 // a):
        c = a * b
        num = str(a) + str(b) + str(c)
        if len(num) == 9 and check_pan_digital(num, 9):
            ans.append(c)
ans = set(ans)
print(sum(ans))
