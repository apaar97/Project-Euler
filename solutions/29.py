#   Distinct powers

x = []
for a in range(2, 101):
    for b in range(2, 101):
        x.append(a ** b)

print(len(set(x)))
