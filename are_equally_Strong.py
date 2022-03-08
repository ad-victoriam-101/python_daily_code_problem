def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    """
    two people are determined to be equally strong if, their Min and Max weights are the same regardless of which arm 
    that is. 
    :param yourLeft: int, 
    :param yourRight: int,
    :param friendsLeft: int,
    :param friendsRight: int,
    :return: a boolean value, if the two people are equally strong. 
    """
    return max(yourLeft, yourRight) == max(friendsLeft, friendsRight) and min(yourLeft, yourRight) == min(friendsLeft,
                                                                                                          friendsRight)
"""
Another solution is as follows, remember that a {} is considered a set in python and sorts the values. 
"""
def solution2(yourLeft, yourRight, friendsLeft, friendsRight):
    print({yourLeft, yourRight},{friendsLeft,friendsRight})
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}

assert solution(10, 15, 15, 10) == True
