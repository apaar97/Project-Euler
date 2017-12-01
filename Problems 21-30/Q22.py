#   Names scores

with open('input22.txt', 'r') as f:
    a = (f.read().strip().split(','))
f.close()
a.sort()
ans = 0
for i in range(len(a)):
    ans += sum((ord(c) - 64) for c in a[i][1:-1]) * (i + 1)
print(ans)
