#   Multiples of 3 and 5


def multiple_3_or_5(limit):
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            yield i


print(sum(multiple_3_or_5(1000)))
