#   Circular primes

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


def rotate(l, n):
    return l[n:] + l[:n]


def check_circular_prime(n):
    for i in range(1, len(n)):
        num = int(rotate(n, i))
        if num not in prime:
            return False
    return True


sieve(1000000)
prime = set(prime)
ans = 0
for i in prime:
    if i < 1000000 and check_circular_prime(str(i)):
        ans += 1
print(ans)
