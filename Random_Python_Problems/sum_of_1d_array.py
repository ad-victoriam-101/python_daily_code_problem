"""
Given an array nums. We define a running sum of an array a runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""


class Solution:
    def runnin_sum(self, nums: List[int]) -> List[int]:
        start = 0
        return_list = []
        for i in range(len(nums)):
            return_list.append(nums[i] + start)
            start += nums[i]
        return return_list
