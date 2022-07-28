from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums == None or len(nums) == 0:
            return False
        else:
            sorted_nums = (sorted(nums))
            for i in range(len(sorted_nums) - 1):
                if sorted_nums[i] == sorted_nums[i + 1]:
                    return True
            return False


print(Solution.containsDuplicate(nums=[1, 2, 3, 4, 5, 1]))
