
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            #python MAX() returns the max between two values

            curSum = max(curSum, 0) + num
            maxSum = max(maxSum, curSum)

        return maxSum