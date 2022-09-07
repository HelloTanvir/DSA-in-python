def findFirstIndex(nums: list[int], target: int) -> int:
    res = -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            res = mid
            right = mid - 1

    return res

def findLastIndex(nums: list[int], target: int, left: int) -> int:
    res = left

    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid - 1
        else:
            res = mid
            left = mid + 1

    return res

def findFirstAndLastIndex(nums: list[int], target: int) -> int:
    firstIndex = findFirstIndex(nums, target)
    
    if firstIndex == -1:
        lastIndex = -1
    else:
        lastIndex = findLastIndex(nums, target, firstIndex)

    return [firstIndex, lastIndex]
