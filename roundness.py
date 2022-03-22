def solution(n):
    """
    Given an integer n, check if it's possible to increase n's roundness by swapping some pair of its digits.
    :param n:
    :return:
    """
    string_n = str(n)
    rev_n = string_n[::-1]
    for i in string_n[::-1]:
        if i == '0':
            rev_n = rev_n.replace(i, '', 1)
        else:
            break
    return '0' in rev_n


print(solution(902200100))

assert solution(11000) == False
assert solution(902200100) == True
