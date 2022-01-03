#   Coin Sums

cache = {}
coins = [1, 2, 5, 10, 20, 50, 100, 200]


def coin_change(curr, sum):
    if sum == 0: return 1
    if sum < 0: return 0
    if curr == len(coins): return 0
    if (curr, sum) not in cache:
        cache[(curr, sum)] = coin_change(curr, sum - coins[curr]) + coin_change(curr + 1, sum)
    return cache[(curr, sum)]


print(coin_change(0, 200))
