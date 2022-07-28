"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def solution(nums, target):
    for left in range(len(nums) - 1):
        right = left + 1
        while right < len(nums):
            if nums[left] + nums[right] == target:
                print([left, right])
            right += 1


def solution_2(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_map:
            return [i, hash_map[complement]]
        hash_map[nums[i]] = i


print(solution_2([2, 7, 11, 15], 9))
print(solution([3, 2, 4], 6))
