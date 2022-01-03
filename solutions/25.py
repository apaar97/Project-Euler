#   1000-digit Fibonacci number


def fib(terms):
    x, y = 1, 1
    i = 1
    while i < terms:
        yield x
        x, y = y, x + y
        i += 1


i = 1
for x in fib(10000):
    if len(str(x)) >= 1000:
        print(i)
        break
    i += 1
