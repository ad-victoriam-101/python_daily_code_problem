"""
in this problem we are asked to return the unique
single value from a given list of repeating values.
"""
import operator
from functools import reduce


class Solution:
    def single_number(self, nums):
        return reduce(operator.xor, nums)
