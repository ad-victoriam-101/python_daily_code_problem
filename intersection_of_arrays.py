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
    from collections import Counter
    # nums1_dic = {}
    # nums2_dic = {}
    # return_list = []
    # for i in nums1:
    #     if i not in nums1_dic:
    #         nums1_dic[i] = 1
    #     else:
    #         nums1_dic[i] += 1
    # for j in nums2:
    #     if j not in nums2_dic:
    #         nums2_dic[j] = 1
    #     else:
    #         nums2_dic[j] += 1
    # for k in nums1_dic.keys():
    #     if k in nums2_dic.keys():
    #         return_list.append(k)
    #
    # return return_list
    nums1_dic,nums2_dic = Counter(nums1),Counter(nums2)
    return_list = []
    for i in nums1_dic.keys():
        if i in nums2_dic.keys():
            return_list.append(i)
    return return_list


print(solution([4, 9, 5, 4], [9, 4, 9, 8, 4, 5]))
