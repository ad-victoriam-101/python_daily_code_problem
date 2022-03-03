def solution(inputString):
    """
    given an input string, find out if its characters can be rearranged to form a palindrome.

    :param inputString: string of characters, 1<=input string<=50
    :return: a True False value if it can be or can not be palindromed.
    """
    # palendromes can only be if at most one character is odd, this checks to make sure that there is only 1
    # non even character.
    return sum([inputString.count(i) % 2 for i in set(inputString)]) <= 1


assert solution('aabb') == True
