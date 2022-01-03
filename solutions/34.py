#   Digit factorials


fact = [0] * 10
fact[0] = 1
for i in range(1, 10):
    fact[i] = fact[i - 1] * i


def digit_fact_sum(n):
    res = 0
    while n:
        res += fact[n % 10]
        n //= 10
    return res


limit = 7 * fact[9]
ans = 0
for i in range(10, limit):
    if digit_fact_sum(i) == i:
        ans += i
print(ans)
