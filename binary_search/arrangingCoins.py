def arrangingCoins(coins: int) -> int:
    l, r, res = 1, coins, 0

    while l <= r:
        mid = l + ((r - l) // 2)
        neededCoins = coins * (coins + 1) / 2

        if neededCoins > coins:
            r = mid - 1
        else:
            res = max(res, mid)
            l = mid + 1

    return res
