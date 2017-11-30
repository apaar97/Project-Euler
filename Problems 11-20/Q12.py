#   Highly divisible triangular number

prime = []


def sieve(limit):
    sv = [0] * (limit + 1)
    sv[0], sv[1] = 1, 1
    i = 2
    while i * i <= limit:
        if not sv[i]:
            j = i * i
            while j <= limit:
                sv[j] = 1
                j += i
        i += 1
    for i in range(limit):
        if not sv[i]:
            prime.append(i)


def num_div(n):
    cnt = 1
    for i in prime:
        if n > 1 and n % i == 0:
            x = 0
            while n % i == 0:
                n = n // i
                x += 1
            cnt *= (x + 1)
    return cnt


sieve(1000000)
n = 1
i = 2
while (num_div(n) < 500):
    n += i
    i += 1
print(n)
