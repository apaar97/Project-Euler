#   Even Fibonacci numbers


def even_fib(limit):
    x, y = 0, 1
    while x < limit:
        if not x % 2:
            yield x
        x, y = y, x + y


print(sum(even_fib(4000000)))
