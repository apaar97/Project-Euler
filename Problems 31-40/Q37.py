#   Truncatable primes


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


def is_truncable(n):
    for i in range(1, len(n)):
        if int(n[i:]) not in prime or int(n[:i]) not in prime:
            return False
    return True


ans = []
sieve(1000000)
prime = set(prime)
for n in prime:
    if n > 10 and is_truncable(str(n)):
        ans.append(n)

print(sum(ans))
