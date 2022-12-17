class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        """

        Args:
            nums: list of ints contains both positive
            and negative values

        Returns:
            the maximum sum of possible values.

        """


        curSum = maxSum = nums[0]
        for num in nums[1:]:
            # python MAX() returns the max between two values

            curSum = max(curSum, 0) + num
            maxSum = max(maxSum, curSum)

        return maxSum
