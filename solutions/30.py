#   Digit fifth powers


def digit_power_sum(n, p):
    res = 0
    while n:
        res += (n % 10) ** p
        n //= 10
    return res


power = 5
ans = 0
limit = power * (9 ** power)
for i in range(2, limit):
    if digit_power_sum(i, power) == i:
        ans += i
print(ans)
