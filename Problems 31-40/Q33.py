#   Digit cancelling fractions

'''
    Numbers will be of form

    (10n + i) / (10i + d) = n / d

        =>  (10n + i)d = (10i + d)n

                n < d < i
'''

import math

dprod = 1
nprod = 1
for i in range(1, 10):
    for n in range(1, 10):
        for d in range(1, 10):
            if (10 * n + i) * d == (10 * i + d) * n:
                nprod *= n
                dprod *= d
dprod //= math.gcd(nprod, dprod)
print(dprod)
