def findRotationCount(nums: list[int]) -> int:
    # assuming the list doesn't contain repeating number
    # the position of the smallest number is also the rotation count
    # [4, 5, 6, 1, 2, 3]
    # here the array is rotated 3 times
    # also the position of the smallest number is 3
    # so I need to find the position of the smallest number and return it

    assert len(nums) > 0, 'the list is empty'

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid + 1

    return right
