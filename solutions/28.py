#   Number spiral diagonals

'''
    f(n) = f(n-2) + 2(n-1)(2n-1)+4
'''


def f(n):
    if n == 1:
        return 1
    else:
        return f(n - 2) + 2 * (n - 1) * (2 * n - 1) + 4


print(f(1001))
