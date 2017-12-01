#   Integer right triangles

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
    cnt = 0
    limit = int(math.sqrt(sum // 2))
    for m in range(2, limit + 1):
        if sum // 2 % m == 0:
            if m % 2 == 0:
                k = m + 1
            else:
                k = m + 2
            while k < 2 * m and k <= sum // (2 * m):
                if (sum // 2 * m) % k == 0 and math.gcd(m, k) == 1:
                    cnt += 1
                k += 2
    return cnt


ans = 0
max = 0
for i in range(1, 1001):
    sol = f(i)
    if sol > max:
        max = sol
        ans = i
print(ans)
