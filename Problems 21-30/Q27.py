#   Quadratic primes


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


def f(a, b, n):
    return n * n + a * n + b


max = 0
ans = 0
sieve(1000)
for a in range(-999, 999):
    for b in prime:
        n = 0
        while True:
            if not f(a, b, n) in prime:
                break
            n += 1
        if n > max:
            max = n
            ans = a * b
        n = 0
        while True:
            if not f(a, -b, n) in prime:
                break
            n += 1
        if n > max:
            max = n
            ans = a * b

print(ans)
