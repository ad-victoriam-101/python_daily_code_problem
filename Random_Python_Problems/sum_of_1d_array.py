"""
Given an array nums. We define a running sum of an array a runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""
import itertools


class Solution:
    def runnin_sum(self, nums: list[int]) -> list[int]:
        start = 0
        return_list = []
        for i in range(len(nums)):
            return_list.append(nums[i] + start)
            start += nums[i]
        return return_list

    def one_liner(self, nums: list[int]) -> list[int]:
        return list(itertools.accumulate(nums))


solution = Solution()
solution.runnin_sum([1,2,3,4])
print(solution.one_liner([1,2,3,4]))

