#   Largest prime factor


def largest_prime_factor(n):
    i = 2
    num = n
    while i * i <= num:
        while n % i == 0:
            n //= i
        if n == 1:
            return i
        elif i == 2:
            i += 1
        else:
            i += 2
    return n


print(largest_prime_factor(600851475143))
