#   Longest Collatz sequence


def collatz(n):
    cnt = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        cnt += 1
    return cnt


ans = 0
num = 1
for i in range(2, 1000000):
    res = collatz(i)
    if res > ans:
        ans = res
        num = i

print(num)
