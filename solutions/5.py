#   Smallest multiple


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


ans = 1
for i in range(2, 21):
    ans = lcm(ans, i)
print(ans)
