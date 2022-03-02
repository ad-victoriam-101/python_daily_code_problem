"""
Given integers n,l and r. fint the number of ways to represent n
as a sum of two ints A,B such that l<=A<=B<=r

:param n: integer
:param l: integer
:param r: integer
"""


def solution(n, l, r):
    """
    :param n: int
    :param l: integer
    :param r: integer
    :return: int
    """
    # return_numbers = 0
    # for i in range(l, r + 1):
    #     print(i)
    #     for j in range(l, r + 1):
    #         if i + j == n and i <= j:
    #             #print(i, j)
    #             return_numbers += 1
    #     i = j
    #
    # return return_numbers
    return sum(1 for a in range(l, r+1) if l <= a <= n-a <= r)


assert (solution(6, 2, 4)) == 2
