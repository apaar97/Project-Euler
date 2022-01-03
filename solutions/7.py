#   10001st prime


def sieve(limit):
    sv = [0] * (limit + 1)
    prime = []
    i = 2
    while i <= limit:
        if not sv[i]:
            prime.append(i)
            j = i * i
            while j <= limit:
                sv[j] = 1
                j += i
        i += 1
    return prime


prime_list = sieve(200000)
print(prime_list[10000])
