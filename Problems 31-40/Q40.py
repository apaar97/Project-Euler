#   Champernowne's constant

N = 10 ** 6
num = '0'
for i in range(1, N + 1):
    num += str(i)
    if len(num) > N:
        break
ans = 1
for i in range(1, 7):
    ans *= int(num[10 ** i])
print(ans)
