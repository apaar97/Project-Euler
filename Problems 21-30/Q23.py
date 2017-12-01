#   Non-abundant sums


def sum_div(n):
    res = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                res += i
            else:
                res += i
                res += n // i
        i += 1
    return res - n


N = 28123
sv = [0] * (N + 1)
a = []


def sieve_abudant(limit):
    for i in range(limit):
        if sum_div(i) > i:
            a.append(i)


def sieve_abudant_sum(limit):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] + a[j] < limit:
                sv[a[i] + a[j]] = 1


ans = 0
sieve_abudant(N + 1)
sieve_abudant_sum(N + 1)
for i in range(len(sv)):
    if not sv[i]:
        ans += i
print(ans)
