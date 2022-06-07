"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def solution(nums, target):
    left = 0
    right = 1
    while right < len(nums)-1:
        print(left,right)
        right += 1


print(solution([2, 7, 11, 15], 9))
print(solution([3, 2, 4], 6))
