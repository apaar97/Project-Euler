#   Sum square difference


def f(n):
    x = n * (n + 1) // 2
    y = n * (n + 1) * (2 * n + 1) // 6
    return x * x - y


print(f(100))
