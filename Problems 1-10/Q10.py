#   Summation of primes

def gen_prime(limit):
    sv = [0] * (limit + 1)
    i = 2
    while i <= limit:
        if not sv[i]:
            yield i
            j = i * i
            while j <= limit:
                sv[j] = 1
                j += i
        i += 1

N = 2000000
print(sum(gen_prime(N)))