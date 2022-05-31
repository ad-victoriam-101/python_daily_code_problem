def maxSubArray(nums):
    max_tbd = nums[0]
    max_cur = nums[0]

    for i in range(1, len(nums)):
        max_cur = max(nums[i], max_cur + nums[i])
        max_tbd = max(max_tbd, max_cur)
    return max_tbd


print(maxSubArray([1, -3, 2, -4, 1, 4, -5, 1, 2, 3, -4]))
