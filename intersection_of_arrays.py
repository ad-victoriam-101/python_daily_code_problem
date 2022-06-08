"""
Given two integer arrays nums1 and nums2,
return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.
"""


def solution(nums1, nums2):
    """
    Args:
        nums1: list of ints
        nums2: list of ints

    Returns:
        list of each element that appears in each array.
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2,2]
    """
    print([i for i in nums1 if i in nums2])


solution([4, 9, 5, 4], [9, 4, 9, 8, 4, 5])
