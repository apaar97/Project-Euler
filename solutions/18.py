#   Maximum path sum I

a = []
with open('inputs/18.txt', 'r') as f:
    for line in f:
        a.append([int(x) for x in line.strip().split(' ')])

for i in range(len(a[-1]) - 2, -1, -1):
    for j in range(len(a[i])):
        a[i][j] += max(a[i + 1][j], a[i + 1][j + 1])

print(a[0][0])
