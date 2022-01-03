#   Special Pythagorean triplet

import math

'''
    a^2+b^2=c^2
    a + b + c = s
        c>b>a>0

    a = d*(m^2-n^2)
    b = d*(2*m*n)
    c = d*(m^2+n^2)
        m>n>0

    2*d*m*(m+n) = s
'''


def f(sum):
    limit = int(math.sqrt(sum // 2))
    for m in range(2, limit + 1):
        if sum // 2 % m == 0:
            if m % 2 == 0:
                k = m + 1
            else:
                k = m + 2
            while k < 2 * m and k <= sum // (2 * m):
                if (sum // 2 * m) % k == 0 and math.gcd(m, k) == 1:
                    n = k - m
                    d = sum // (2 * k * m)
                    a = d * (m ** 2 - n ** 2)
                    b = d * (2 * m * n)
                    c = d * (m ** 2 + n ** 2)
                    return a * b * c
                k += 2


print(f(1000))
