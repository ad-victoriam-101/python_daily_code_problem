"""
Given a string given the longest constant substring that contains at most 2 unique characters

"""


def len_of_two_sub_strings(string):
    """

    Args:
        string: random string of letters,

    Returns: longest sub set of letters

    """
    max_char = 0
    left = 0
    right = 1
    def is_two_char(st):
        return len(set(st))<=2


    while (left < right):
        if is_two_char(string[left:right]) and right < len(string):
            max_char = max(max_char, len(string[left:right]))
            right += 1
        elif is_two_char(string[left:right]) and right == len(string):
            return max(max_char, len(string[left:right]))
        else:
            left += 1

    return max_char

print(len_of_two_sub_strings("ababccde"))

def lengthOfLongestSubstringTwoDistinct(s):
    maxLen = 0  # this will be returned at the end, and it maintains my current max found
    # s[right:left], s.substring(0,1)
    left = 0
    right = 1

    def isAtMostTwoChars(st):
        return len(set(st)) <= 2

    while (left < right):  # since I move both flags, left will eventually hit right once right hits the end
        if isAtMostTwoChars(s[left:right]) and right < len(s):
            maxLen = max(maxLen, len(s[left:right]))
            right += 1
        elif isAtMostTwoChars(s[left:right]) and right == len(s):
            return max(maxLen, len(s[left:right]))
        else:
            left += 1

    return maxLen
print(lengthOfLongestSubstringTwoDistinct("ababccde"))