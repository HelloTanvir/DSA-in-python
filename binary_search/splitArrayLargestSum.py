def splitArray(nums: list[int], m: int) -> int:
    def canSplit(largest: int) -> int:
        subArray = 0
        currentSum = 0
        for n in nums:
            currentSum += n
            if currentSum > largest:
                subArray += 1
                currentSum = n
        return subArray + 1 <= m

    l, r = max(nums), sum(nums)
    res = r
    while l <= r:
        mid = l + ((r - l) // 2)
        if canSplit(mid):
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res
