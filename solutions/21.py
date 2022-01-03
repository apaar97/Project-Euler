#   Amicable numbers


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


N = 10000
s = [sum_div(i) for i in range(N)]
ans = 0
for i in range(1, N):
    if s[i] < N and s[i] != i and s[s[i]] == i:
        ans += i
print(ans)
