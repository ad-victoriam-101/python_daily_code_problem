
def kadanes_algorithm(nums[])
    curSum = maxSum = A[0]
    for num in A[1:]:
        curSum = max(curSum, 0) + num
        maxSum = max(maxSum, curSum)

    return maxSum