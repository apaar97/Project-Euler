#   Largest palindrome product


def largest_palindrome():
    ans = 0
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            k = i * j
            if str(k) == str(k)[::-1]:
                ans = max(ans, k)
    return ans


print(largest_palindrome())
