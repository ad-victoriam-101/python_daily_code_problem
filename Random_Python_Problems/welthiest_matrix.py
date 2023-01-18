"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith​​​​
customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
"""


class Solution:
    def max_wealth(self, account: list[list[int]]) -> int:
        cur_max = 0
        for customer in account:
            if sum(customer) >= cur_max:
                cur_max = sum(customer)
        print(customer, cur_max)

    def max_wealth_sum(self, account: list[list[int]]) -> int:
        return max([sum(customer) for customer in account])

    def max_sum_map(self, account: list[list[int]]) -> int:
        return max(map(sum,account))


s = Solution()

print(s.max_wealth([[1, 2, 3], [4, 5, 6]]))
print(s.max_wealth_sum([[1, 2, 3], [4, 5, 6]]))
