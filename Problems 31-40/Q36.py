#   Double-base palindromes


def check_palindrome(s):
    return s == s[::-1]


ans = 0
for i in range(1, 1000000):
    if check_palindrome(str(i)) and check_palindrome(str(bin(i)[2:])):
        ans += i
print(ans)
