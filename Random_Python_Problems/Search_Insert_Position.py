import bisect


def bisect_search(nums: List[int], target: int) -> int:
    """
    Args:
        nums: List of distinct integers,
        target: int: value either within nums or not
    Returns:
        IF the target is in nums: returns the index of the target.
        ELSE: returns the index where it would be inserted in order.

    """
    # Bisect Module
    # import bisect assumed.
    return bisect.bisect_left(nums, target)


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        """
        Args:
            nums: List of distinct integers,
            target: int: value either within nums or not

        Returns:
            IF the target is in nums: returns the index of the target.
            ELSE: returns the index where it would be inserted in order.

        """

        # Linear Search
        if not nums:
            return 0
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)



