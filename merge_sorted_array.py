"""
You are given two integer arrays nums1 and nums2,
sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
"""


def solution(nums1, m, nums2, n):
    nums1 = sorted(nums1[:m] + nums2[:n])
    print(nums1)




def solution_2(nums1, m, nums2, n):
    i = 0
    for j in range(len(nums1)):
        if i >= n:
            break
        if nums1[j] == 0:
            nums1[j] = nums2[i]
            i += 1
    nums1.sort()


print(solution_2([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
(solution([1], 1, [], 0))
(solution([0], 0, [1], 1))
