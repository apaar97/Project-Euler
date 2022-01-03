#   Pandigital prime

from functools import reduce

prime = []


def sieve(limit):
    i = 2
    sv = [0] * limit
    sv[0] = 1
    sv[1] = 1
    while i < limit:
        if not sv[i]:
            prime.append(i)
            j = i * i
            while j < limit:
                sv[j] = 1
                j += i
        i += 1


def check_pan_digital(n, digits):
    a = (reduce(lambda rst, d: rst * 10 + d, range(1, digits + 1)))
    n = ''.join(sorted(n))
    return int(n) == a


N = 7654321
sieve(N + 1)
prime = set(prime)
for i in range(N, 1234, -1):
    if i in prime and check_pan_digital(str(i), len(str(i))):
        print(i)
        break
