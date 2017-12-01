#   Reciprocal cycles


def count_rep_digit(n):
    a = []
    rem = 1
    while rem:
        while rem < n:
            rem *= 10
        rem = rem % n
        if rem in a:
            return len(a) - a.index(rem)
        else:
            a.append(rem)
    return 0


max = 0
ans = 1
for d in range(2, 1000):
    l = count_rep_digit(d)
    if l > max:
        max = l
        ans = d

print(ans)
